#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

rospy.init_node("disparity_map")

pub = rospy.Publisher('disparity_map', Image, queue_size=0)

img = cv2.imread("/home/ailand/Pictures/Disparity_Image.jpeg")
ros_img = CvBridge().cv2_to_imgmsg(img)

while not rospy.is_shutdown():
    pub.publish(ros_img)

    rospy.Rate(100).sleep