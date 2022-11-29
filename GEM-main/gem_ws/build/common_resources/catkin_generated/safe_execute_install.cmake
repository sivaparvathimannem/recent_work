execute_process(COMMAND "/home/ailand/GEM-main/gem_ws/build/common_resources/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/ailand/GEM-main/gem_ws/build/common_resources/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
