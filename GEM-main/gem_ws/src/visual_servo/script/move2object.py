#!/usr/bin/env python3

import rospy
from etasb_msgs.msg import point2DArray
from sensor_msgs.msg import Image
from move2point import moveit_driver
import time

height = 1.8

def macro_movement(driver, target, img_dim):
  ''' Function for big movement
  '''

  # Area 1: upper section
  if target[1] < img_dim[1]/2:
    print("moving to top section")
    driver.go_to_joint_state([-1.571, 0, 0, 0, -1.571, 0])

  # Area 2: bottom left section
  elif target[0] < img_dim[0]/2:
    print("moving to bottom left section")
    driver.go_to_joint_state([0, 0, 0, 0, -1.571, 0])

  print("macro movement complete!")
def rough_alignment(driver, target):
  ''' Aligning the end effector so that the effector camera can see the object
  '''
  def cam2world(point):
    '''Converting from camera to world coordinate'''
    m_per_pixel = 0.001
    offset = [0.884, -0.95]

    new_point = [0, 0]
    new_point[0] = offset[0] - m_per_pixel * point[0]
    new_point[1] = offset[1] + m_per_pixel * point[1]

    return new_point

  # convert from camera to world coordinate
  world_target = cam2world(target)

  target_pose = driver.getPose()

  target_pose[0] = world_target[0]
  target_pose[1] = world_target[1]
  target_pose[2] = height

  # make end effector face down
  target_pose[3] = -0.002793788376135
  target_pose[4] = -0.002425824313289
  target_pose[5] = -0.710762988400535
  target_pose[6] = 0.703421839611801

  driver.moveto_xyzrpy(target_pose)

  print("rough alignment complete!")

def fine_alignment(driver, tolerance=0.1):
  '''Align the target in the middle of the robot camera
  '''
  tolerance
  aligned = False
  img_msg = rospy.wait_for_message("/robot_depth_camera/color/image_raw", Image)
  img_dim = [img_msg.width, img_msg.height]
  mid = [i/2 for i in img_dim]

  while not aligned:
    target_msg = rospy.wait_for_message("/robot_depth_camera/color/image_raw/chain", point2DArray)
    target = [target_msg.x[0], target_msg.y[0]]
    
    target_pose = driver.getPose()

    if target[0] < mid[0] - mid[0]*tolerance:
      target_pose[0] += 0.05
    elif target[0] > mid[0] + mid[0]*tolerance:
      target_pose[0] -= 0.05
    elif target[1] < mid[1] - mid[0]*tolerance:
      target_pose[1] -= 0.05
    elif target[1] > mid[1] + mid[0]*tolerance:
      target_pose[1] += 0.05
    else:
      print("fine alignment complete!")
      aligned = True

    driver.moveto_xyzrpy(target_pose)

    time.sleep(2)

def moving_down(driver):
  target_pose = driver.getPose()
  target_pose[2] = 1.5
  driver.moveto_xyzrpy(target_pose)


if __name__ == '__main__':
  rospy.init_node("motor_servo")

  # activate the moveit driver
  armDriver = moveit_driver.arm_driver()

  #region Macro-position *******************
  
  print("Moving to target position!")

  # get the target
  target_msg = rospy.wait_for_message("/top_depth_camera/color/image_raw/chain", point2DArray)
  target = [target_msg.x[0], target_msg.y[0]]
  img_msg = rospy.wait_for_message("/top_depth_camera/color/image_raw", Image)
  img_dim = [img_msg.width, img_msg.height]

  macro_movement(armDriver, target, img_dim)

  rough_alignment(armDriver, target)

  fine_alignment(armDriver)
  
  moving_down(armDriver)