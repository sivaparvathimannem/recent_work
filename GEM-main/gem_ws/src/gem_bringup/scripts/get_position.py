#!/usr/bin/env python3

from move2point import moveit_driver
import rospy

if __name__ == '__main__':
  rospy.init_node("get_position_node")
  armDriver = moveit_driver.arm_driver()
  print("position values")
  print(armDriver.group.get_current_pose().pose)
  print("joint values:")
  joint_states = [round(item, 3) for item in armDriver.group.get_current_joint_values()]
  print(joint_states)