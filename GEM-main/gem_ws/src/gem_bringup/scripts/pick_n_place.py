#!/usr/bin/env python3

from move2point import moveit_driver
import rospy

armDriver = moveit_driver.arm_driver()
gripperDriver = moveit_driver.gripper_driver()
carriageDriver = moveit_driver.carriage_driver()

prepick1 = [-1.5708, 0.3992, 0.8852, 0, -1.996, 0]
prepick2 = [-1.5708, 1.5447, 0, 0, 0, 0]
pick = [-1.5708, 1.8918, 0.3298, 0, 0, 0]
place = [1.5708, 0.3992, 0.8852, 0, -1.996, 0]

def pick_n_place():
  global armDriver, gripperDriver
  armDriver.go_to_joint_state(prepick1)
  armDriver.go_to_joint_state(prepick2)
  gripperDriver.open()
  armDriver.go_to_joint_state(pick)
  gripperDriver.close()
  armDriver.go_to_joint_state(prepick1)
  armDriver.go_to_joint_state(place)
  gripperDriver.open()

def main():
  try:
    carriageDriver.go_to_joint_state([-0.667])
    pick_n_place()
    carriageDriver.go_to_joint_state([-0.317])
    pick_n_place()
    carriageDriver.go_to_joint_state([0.033])
    pick_n_place()
    carriageDriver.go_to_joint_state([0.383])
    pick_n_place()

  except rospy.ROSInterruptException:
    return
  except KeyboardInterrupt:
    return

if __name__ == '__main__':
  main()

