# Install script for directory: /home/emanelsayed/ROSProject/catkin_ws/src/navigation_tutorials/roomba_stage

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/emanelsayed/ROSProject/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/emanelsayed/ROSProject/catkin_ws/build/navigation_tutorials/roomba_stage/catkin_generated/installspace/roomba_stage.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roomba_stage/cmake" TYPE FILE FILES
    "/home/emanelsayed/ROSProject/catkin_ws/build/navigation_tutorials/roomba_stage/catkin_generated/installspace/roomba_stageConfig.cmake"
    "/home/emanelsayed/ROSProject/catkin_ws/build/navigation_tutorials/roomba_stage/catkin_generated/installspace/roomba_stageConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roomba_stage" TYPE FILE FILES "/home/emanelsayed/ROSProject/catkin_ws/src/navigation_tutorials/roomba_stage/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roomba_stage" TYPE DIRECTORY FILES "/home/emanelsayed/ROSProject/catkin_ws/src/navigation_tutorials/roomba_stage/maps")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roomba_stage" TYPE DIRECTORY FILES "/home/emanelsayed/ROSProject/catkin_ws/src/navigation_tutorials/roomba_stage/params")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roomba_stage" TYPE FILE FILES
    "/home/emanelsayed/ROSProject/catkin_ws/src/navigation_tutorials/roomba_stage/move_base_lse_arena.launch"
    "/home/emanelsayed/ROSProject/catkin_ws/src/navigation_tutorials/roomba_stage/roomba_lse_arena.world"
    "/home/emanelsayed/ROSProject/catkin_ws/src/navigation_tutorials/roomba_stage/roomba_stage.rviz"
    )
endif()

