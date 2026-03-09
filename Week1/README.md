# Week 1 – ROS 2 Lab

## Brief Description

This lab introduced the basic concepts of ROS 2 and Linux required for robotics development. In this lab, a ROS 2 workspace was created and a Python package named `my_first_pkg` was developed. A simple ROS 2 node (`simple_node`) was implemented and executed using `ros2 run`. The lab also involved understanding the structure of ROS 2 packages, the purpose of `setup.py`, and how nodes are registered as executables.

---

## Commands Used

```bash
# Check ROS2 version
dpkg -s ros-humble-desktop | grep Version

# Source ROS2 environment
source /opt/ros/humble/setup.bash

# Create workspace
mkdir -p ~/Saram_ros2_ws/src
cd ~/Saram_ros2_ws

# Build workspace
colcon build

# Source workspace
source install/setup.bash

# Create ROS2 package
cd ~/Saram_ros2_ws/src
ros2 pkg create --build-type ament_python my_first_pkg

# Build again after creating package
cd ~/Saram_ros2_ws
colcon build
source install/setup.bash

# Check package list
ros2 pkg list | grep my_first_pkg

# Run node
ros2 run my_first_pkg simple_node
```

---

## Problems Faced and Solutions

**Problem 1:** `ros2: command not found`
**Solution:** The ROS 2 environment was not sourced. Running
`source /opt/ros/humble/setup.bash` solved the issue.


**Problem 2:** Node executable not found
**Solution:** The entry point in `setup.py` was not registered correctly. After correcting it and rebuilding the workspace with `colcon build`, the node executed successfully.

---

## Reflection

This lab helped me understand the basic workflow of ROS 2 development. I learned how to create and organize a ROS 2 workspace and how packages are structured. Implementing a simple node helped me understand how ROS 2 runs Python code as executable nodes. I also learned the importance of sourcing the ROS environment and workspace so that ROS 2 can locate packages and executables. Working with `colcon build` showed how ROS 2 compiles and installs packages. The lab also improved my familiarity with Linux terminal commands. Overall, this lab provided a strong foundation for developing robotics applications using ROS 2.
