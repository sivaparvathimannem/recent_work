#!/usr/bin/env python3

from move2point import send_goal
import rospy

def main():
  try:
    armDriver = send_goal.arm_driver()
    gripperDriver = send_goal.gripper_driver()

    # go to the point above the object
    armDriver.moveto_xyzrpy([0, -0.8, 0.8, 0, 0, 0])
    # open the gripper
    gripperDriver.open()
    # move downward
    armDriver.moveto_xyzrpy([0, -0.8, 0.65, 0, 0, 0])
    # close the gripper
    gripperDriver.close()
    # lift the object
    armDriver.moveto_xyzrpy([0, -0.8, 1, 0, 0, 0])
    # go to basket
    # drop item
    gripperDriver.open()
  except rospy.ROSInterruptException:
    return
  except KeyboardInterrupt:
    return

if __name__ == '__main__':
  main()

