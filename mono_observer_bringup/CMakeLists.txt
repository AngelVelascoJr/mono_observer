cmake_minimum_required(VERSION 3.8)
project(mono_observer_bringup)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED) #for python scripts
#find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED) #for python scripts
#find_package(geometry_msgs REQUIRED)
#find_package(nav_msgs REQUIRED)
#find_package(tf2 REQUIRED)
find_package(std_msgs REQUIRED)
find_package(control_msgs REQUIRED) #for ros control

find_package(mujoco_ros2_control REQUIRED)

install(
DIRECTORY launch rviz src
DESTINATION share/${PROJECT_NAME}/
)


# Install Python modules
ament_python_install_package(${PROJECT_NAME})

# Install Python executables #They must start with the shebag tag
install(PROGRAMS
  ${PROJECT_NAME}/src/TestIKPosition.py
  ${PROJECT_NAME}/src/TestIKInputPosition.py
  ${PROJECT_NAME}/src/inverse_kinematics.py
  ${PROJECT_NAME}/src/IKTest.py
  ${PROJECT_NAME}/src/TestAllAngles.py
  ${PROJECT_NAME}/src/Test_multi_tray.py
  DESTINATION lib/${PROJECT_NAME} )

ament_package()
