# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "etasb_msgs: 2 messages, 0 services")

set(MSG_I_FLAGS "-Ietasb_msgs:/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/noetic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(etasb_msgs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2D.msg" NAME_WE)
add_custom_target(_etasb_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "etasb_msgs" "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2D.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2DArray.msg" NAME_WE)
add_custom_target(_etasb_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "etasb_msgs" "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2DArray.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(etasb_msgs
  "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2D.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/etasb_msgs
)
_generate_msg_cpp(etasb_msgs
  "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2DArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/etasb_msgs
)

### Generating Services

### Generating Module File
_generate_module_cpp(etasb_msgs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/etasb_msgs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(etasb_msgs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(etasb_msgs_generate_messages etasb_msgs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2D.msg" NAME_WE)
add_dependencies(etasb_msgs_generate_messages_cpp _etasb_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2DArray.msg" NAME_WE)
add_dependencies(etasb_msgs_generate_messages_cpp _etasb_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(etasb_msgs_gencpp)
add_dependencies(etasb_msgs_gencpp etasb_msgs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS etasb_msgs_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(etasb_msgs
  "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2D.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/etasb_msgs
)
_generate_msg_eus(etasb_msgs
  "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2DArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/etasb_msgs
)

### Generating Services

### Generating Module File
_generate_module_eus(etasb_msgs
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/etasb_msgs
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(etasb_msgs_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(etasb_msgs_generate_messages etasb_msgs_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2D.msg" NAME_WE)
add_dependencies(etasb_msgs_generate_messages_eus _etasb_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2DArray.msg" NAME_WE)
add_dependencies(etasb_msgs_generate_messages_eus _etasb_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(etasb_msgs_geneus)
add_dependencies(etasb_msgs_geneus etasb_msgs_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS etasb_msgs_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(etasb_msgs
  "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2D.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/etasb_msgs
)
_generate_msg_lisp(etasb_msgs
  "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2DArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/etasb_msgs
)

### Generating Services

### Generating Module File
_generate_module_lisp(etasb_msgs
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/etasb_msgs
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(etasb_msgs_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(etasb_msgs_generate_messages etasb_msgs_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2D.msg" NAME_WE)
add_dependencies(etasb_msgs_generate_messages_lisp _etasb_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2DArray.msg" NAME_WE)
add_dependencies(etasb_msgs_generate_messages_lisp _etasb_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(etasb_msgs_genlisp)
add_dependencies(etasb_msgs_genlisp etasb_msgs_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS etasb_msgs_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(etasb_msgs
  "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2D.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/etasb_msgs
)
_generate_msg_nodejs(etasb_msgs
  "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2DArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/etasb_msgs
)

### Generating Services

### Generating Module File
_generate_module_nodejs(etasb_msgs
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/etasb_msgs
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(etasb_msgs_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(etasb_msgs_generate_messages etasb_msgs_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2D.msg" NAME_WE)
add_dependencies(etasb_msgs_generate_messages_nodejs _etasb_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2DArray.msg" NAME_WE)
add_dependencies(etasb_msgs_generate_messages_nodejs _etasb_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(etasb_msgs_gennodejs)
add_dependencies(etasb_msgs_gennodejs etasb_msgs_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS etasb_msgs_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(etasb_msgs
  "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2D.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/etasb_msgs
)
_generate_msg_py(etasb_msgs
  "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2DArray.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/etasb_msgs
)

### Generating Services

### Generating Module File
_generate_module_py(etasb_msgs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/etasb_msgs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(etasb_msgs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(etasb_msgs_generate_messages etasb_msgs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2D.msg" NAME_WE)
add_dependencies(etasb_msgs_generate_messages_py _etasb_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ailand/GEM-main/gem_ws/src/etasb_msgs/msg/point2DArray.msg" NAME_WE)
add_dependencies(etasb_msgs_generate_messages_py _etasb_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(etasb_msgs_genpy)
add_dependencies(etasb_msgs_genpy etasb_msgs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS etasb_msgs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/etasb_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/etasb_msgs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(etasb_msgs_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(etasb_msgs_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/etasb_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/etasb_msgs
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(etasb_msgs_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(etasb_msgs_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/etasb_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/etasb_msgs
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(etasb_msgs_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(etasb_msgs_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/etasb_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/etasb_msgs
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(etasb_msgs_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(etasb_msgs_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/etasb_msgs)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/etasb_msgs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/etasb_msgs
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(etasb_msgs_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(etasb_msgs_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
