#!/usr/bin/env python3

from move2point import send_goal
import rospy

def main():
  try:
    armDriver = send_goal.arm_driver()
    gripperDriver = send_goal.gripper_driver()

    # go to the point above the object
    armDriver.go_to_joint_state([1.37881, -1.64061, -1.58825, 2.89725, 0.0698132, -1.13446])
    # open the gripper
    gripperDriver.open()
    # move downward
    armDriver.go_to_joint_state([1.39626, -1.90241, -1.88496, 2.72271, 0.0349066, -0.959931])
    # close the gripper
    gripperDriver.close()
    # lift the object
    armDriver.go_to_joint_state([1.39626, -1.25664, -1.23918, 2.77507, 0.0523599, -1.02974])
    # go to basket
    armDriver.go_to_joint_state([1.76278, 0.296706, 2.04204, 3.14159, 1.91986, -1.76278])
    # drop item
    gripperDriver.open()
  except rospy.ROSInterruptException:
    return
  except KeyboardInterrupt:
    return

if __name__ == '__main__':
  main()

