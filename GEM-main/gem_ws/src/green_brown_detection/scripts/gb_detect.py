#!/usr/bin/env python3

import cv2
import numpy as np
import time

# import ROS packages
import rospy
from etasb_msgs.msg import point2DArray

from cv_bridge import CvBridge
from sensor_msgs.msg import Image

"""
following https://www.freedomvc.com/index.php/2021/06/06/image-thresholding/
"""

def main(visualize=False):
    rospy.init_node('green_brown_detection')
    
    # print(rospy.get_param_names())
    # print("here")
    topic_name = rospy.get_param('~camera_topic')

    if visualize:
        # create windows in order to dynamically use them
        win_name_color = "color original"
        cv2.namedWindow(win_name_color, cv2.WINDOW_NORMAL)
        win_name_gray = "gray scale image"
        cv2.namedWindow(win_name_gray, cv2.WINDOW_NORMAL)
        win_name_mask = "mask for green"
        cv2.namedWindow(win_name_mask, cv2.WINDOW_NORMAL)
        win_name_contour = "contour"
        cv2.namedWindow(win_name_contour, cv2.WINDOW_NORMAL)
        win_name_final = "final result"
        cv2.namedWindow(win_name_final, cv2.WINDOW_NORMAL)

        cv2.moveWindow(win_name_color, 0, 0)
        cv2.moveWindow(win_name_final, 500, 0)
        cv2.moveWindow(win_name_mask, 0, 500)
        cv2.moveWindow(win_name_gray, 500, 500)
        cv2.moveWindow(win_name_contour, 1000, 500)

    # meta parameters
    updateWhile = time.time()
    updateCycleRect = 0.5
    draw_contour = []   # initialize for delayed drawing. if updateCycleRect is 0.0, it is unnecessary
    draw_center = []
    # minimum contour Area to be recognized
    minContourArea = 100.0
    pixelThresholdLaneAssist = 60
    averageDirection =[]

    bridge = CvBridge()

    while not rospy.is_shutdown():
        # get image topic
        msg = rospy.wait_for_message(topic_name, Image)
        numpy_image_rgb = bridge.imgmsg_to_cv2(msg, desired_encoding='rgb8')

        numpy_image_bgr = cv2.cvtColor(numpy_image_rgb,
                                       cv2.COLOR_RGB2BGR)  # opencv uses BGR images, and converts RGB to BGR
        numpy_image_hsv = cv2.cvtColor(numpy_image_rgb, cv2.COLOR_BGR2HSV)  # hsv to filter out

        # create the mask with in the boundaries
        lower_green = np.array([35, 25, 20])  # all low values
        upper_green = np.array([85, 255, 255])  # all high values
        mask_greenCone = cv2.inRange(numpy_image_hsv, lower_green, upper_green)
        result_greenCone = cv2.bitwise_and(numpy_image_hsv, numpy_image_hsv, mask=mask_greenCone)
        result_bgr = cv2.cvtColor(result_greenCone, cv2.COLOR_HSV2BGR)  # just for display purposes
        result_rgb =cv2.cvtColor(result_bgr, cv2.COLOR_BGR2RGB)

        # We first convert our image into a 3 channel Grayscale image
        image_gray = cv2.cvtColor(numpy_image_bgr, cv2.COLOR_BGR2GRAY)
        image_gray_3 = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)  # reformat into 3 channel image

        # We extract the gray scale version of our image background
        mask_gray_cone = cv2.bitwise_not(mask_greenCone)
        gray_background = cv2.bitwise_and(image_gray_3, image_gray_3, mask=mask_gray_cone)

        # blur the image for cleaner composition
        temp_median = cv2.medianBlur(mask_greenCone, 5)
        for i in range(2):
            temp_gaus = cv2.GaussianBlur(temp_median, (15, 15), 0)
            temp_median = cv2.medianBlur(temp_gaus, 5)

        blur_gaus = cv2.GaussianBlur(temp_median, (15, 15), 0)
        blur_median = cv2.medianBlur(blur_gaus, 5)

        # finding the contour of the green objects (cv2.adaptivethreshold as alternative)
        ret3, th3 = cv2.threshold(blur_median, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(th3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contour_img = gray_background + result_rgb

        # filter contours to eliminate all inside contours, create list of current center points for lane assist and scheduling
        contours_filtered = []
        center_points = []
        center_points_x = []
        center_points_y =[]
        for j, cont in enumerate(contours):
            if hierarchy[0, j, 3] != -1 : continue
            if cv2.contourArea(cont) < minContourArea : continue
            # only relevant cpntours
            contours_filtered.append(cont)
            # get all centroid points of relevant figures
            M = cv2.moments(cont)
            center_points_x.append(int(M["m10"] / M["m00"]))
            center_points_y.append(int(M["m01"] / M["m00"]))
            center_points = list(zip(center_points_x,center_points_y))

        # print rectangles on screen
        for contour in draw_contour:   # draw contour is only updated every updateCycleRect sec
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(contour_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        if time.time() - updateWhile > updateCycleRect:
            draw_contour = contours_filtered
            draw_center = center_points
            updateWhile = time.time()
            # print(draw_center)

        # draw the center points of the objects if any have been found
        if draw_center:
            cv2.drawContours(contour_img, draw_contour, -1, (0, 160, 255), 1)
            for center in draw_center:
                cv2.circle(contour_img, center, 1, (0, 160, 255), -1)
                for centroid in draw_center:
                    if center == centroid:continue
                    if center[1] > centroid[1]:continue
                    if abs(center[0] - centroid[0]) < pixelThresholdLaneAssist:
                        cv2.line(contour_img, center, centroid, (255, 255, 255), 1)

        if visualize:
            # show windows with results
            cv2.imshow(win_name_color, numpy_image_bgr)
            cv2.imshow(win_name_mask, mask_greenCone)
            cv2.imshow(win_name_gray, blur_median)
            cv2.imshow(win_name_contour, contour_img)
            cv2.imshow(win_name_final, gray_background + result_rgb)

            # Press esc to exit the program
            if cv2.waitKey(1) & 0xFF == 27:
                break
        
        contour_pub = rospy.Publisher(topic_name + "/green_contour", Image, queue_size=0)
        contour_pub.publish(bridge.cv2_to_imgmsg(contour_img))
        
        pub = rospy.Publisher(topic_name + "/chain", point2DArray, queue_size=0)
        multi = point2DArray()
        multi.x = center_points_x
        multi.y = center_points_y
        pub.publish(multi)
        
        rospy.Rate(1000).sleep()

if __name__ == "__main__":
    main()