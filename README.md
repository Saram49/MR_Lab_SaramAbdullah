# MR_Lab_2022MC49

## Repository Description

This repository contains the laboratory work completed for the **Mobile Robotics Lab (MCT-454L)** course.
The labs focus on learning the fundamentals of **ROS 2**, Linux-based robotics development, and the software architecture used in modern robotic systems.

---

## About the Course

Mobile Robotics Lab introduces students to the development of robot software using **ROS 2 (Robot Operating System 2)**.
The labs guide students through building ROS 2 workspaces, creating packages, writing nodes, and understanding communication between different components of a robotic system.

---

## Development Environment

The following tools and technologies are used throughout the course:

* Ubuntu Linux
* ROS 2 Humble
* Python
* Colcon Build System
* Git & GitHub

---

## Important Commands

Below are some essential commands frequently used during the labs.

### Source ROS 2 Environment

```bash
source /opt/ros/humble/setup.bash
```

### Build the Workspace

```bash
colcon build
```

### Source the Workspace

```bash
source install/setup.bash
```

### Create a ROS 2 Package

```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python my_first_pkg
```

### List ROS 2 Packages

```bash
ros2 pkg list
```

### Run a Node

```bash
ros2 run <package_name> <executable_name>
```

---
