cmake_minimum_required(VERSION 2.8.3)
project(etasb_msgs)

find_package(catkin REQUIRED
  message_generation
  std_msgs
  actionlib_msgs
  )

add_message_files(DIRECTORY msg FILES
  point2D.msg
  point2DArray.msg
)

generate_messages(DEPENDENCIES
  std_msgs
  actionlib_msgs
)

catkin_package(CATKIN_DEPENDS
  message_runtime
  std_msgs
  actionlib_msgs
)
