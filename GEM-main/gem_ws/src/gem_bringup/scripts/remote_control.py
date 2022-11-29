#!/usr/bin/env python3

from move2point import moveit_driver
import rospy
from getkey import getkey
import os
from common_resources import custom_functions

armDriver = moveit_driver.arm_driver()

def pose2array(pose):
  arr = [
          pose.position.x,
          pose.position.y,
          pose.position.z,
          pose.orientation.x,
          pose.orientation.y,
          pose.orientation.z,
          pose.orientation.w
        ]

  return arr

if __name__ == '__main__':
  rospy.init_node("arm_remote")
  custom_functions.suppress_TF_REPEATED_DATA()
  
  fix_pose = True
  
  while not rospy.is_shutdown():
    
    
    key = getkey()

    os.system('cls' if os.name == 'nt' else 'clear')

    current_pose = armDriver.group.get_current_pose().pose

    if key == "1":
      fix_pose = not fix_pose
      print("fix pose: " + str(fix_pose))  
      
    elif fix_pose:
      if key == "w":
        current_pose.position.x = current_pose.position.x + 0.1
      elif key == "s":
        current_pose.position.x = current_pose.position.x - 0.1
      elif key == "a":
        current_pose.position.y = current_pose.position.y + 0.1
      elif key == "d":
        current_pose.position.y = current_pose.position.y - 0.1
      
      armDriver.cartPlanGo(current_pose)
    
    else:
      if key == "w":
        current_pose.position.x = current_pose.position.x + 0.1
      elif key == "s":
        current_pose.position.x = current_pose.position.x - 0.1
      elif key == "a":
        current_pose.position.y = current_pose.position.y + 0.1
      elif key == "d":
        current_pose.position.y = current_pose.position.y - 0.1

      armDriver.moveto_xyzrpy(pose2array(current_pose))

    rospy.Rate(1000).sleep()