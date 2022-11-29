#!/usr/bin/env python3

import rospy, cv2
from etasb_msgs.msg import point2DArray
import numpy as np

from cv_bridge import CvBridge
from sensor_msgs.msg import Image

if __name__ == "__main__":
    
    rospy.init_node('distortion_correction')
    bridge = CvBridge()
    
    while not rospy.is_shutdown():
        # get image topic
        msg = rospy.wait_for_message("/image_with_contour", Image)
        img = bridge.imgmsg_to_cv2(msg)
        
        dist_pt = np.float32([])
        cv2.imshow('corrected_image', img)
        cv2.waitKey(1) 

        rospy.Rate(10).sleep()