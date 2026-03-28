# Week 3 – ROS 2 Workspace, Package Creation & Turtle Control

## Overview

This lab focuses on setting up a **ROS 2 workspace from scratch**, integrating **GitHub for version control**, creating a **custom ROS 2 package**, and developing a node to control a turtle in specific motion patterns using Turtlesim.

---

## Objectives

* Set up a ROS 2 workspace
* Learn Git and GitHub integration
* Create a ROS 2 Python package
* Develop a ROS 2 node to control turtle motion
* Implement movement patterns (square, circular, triangular)

---

## Prerequisites

Before starting this lab:

* ROS 2 Humble installed
* Basic Linux command knowledge
* Understanding of ROS 2 nodes and topics
* GitHub account

---

## Tools & Technologies

* ROS 2 Humble
* Python
* Turtlesim
* Git & GitHub
* Ubuntu Linux
* VS Code (optional)

---

## Important Commands

### Workspace Setup

```bash id="l3c1"
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
```

### Source Workspace

```bash id="l3c2"
source install/setup.bash
```

### Make Sourcing Permanent

```bash id="l3c3"
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

### Git Configuration

```bash id="l3c4"
sudo apt install git
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

### Initialize Git Repository

```bash id="l3c5"
cd ~/ros2_ws/src
git init
```

### Connect to GitHub

```bash id="l3c6"
git remote add origin <repo_url>
git branch -M main
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

### Create ROS 2 Package

```bash id="l3c7"
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python --dependencies rclpy turtlesim my_turtle_package
```

---

### Build and Source

```bash id="l3c8"
cd ~/ros2_ws
colcon build
source install/setup.bash
```

---

### Run Turtlesim

```bash id="l3c9"
ros2 run turtlesim turtlesim_node
```

### Run Custom Node

```bash id="l3c10"
ros2 run my_turtle_package move_turtle
```

---

## Procedure Summary

1. Created a new ROS 2 workspace and built it using `colcon`.
2. Configured Git and connected the workspace to GitHub.
3. Created a new ROS 2 Python package.
4. Developed a Python node to control turtle movement.
5. Executed the node along with Turtlesim to observe motion patterns.
6. Modified the node to generate different movement trajectories.

---

## Tasks Performed

* Implemented square motion pattern
* Modified code for circular motion
* Implemented triangular motion
* Spawned multiple turtles
* Controlled turtles independently using topics

---

## Observations

* ROS 2 nodes can continuously publish velocity commands to control motion.
* The `/turtle1/cmd_vel` topic is used to control turtle movement.
* Different velocity values produce different motion patterns.
* Multiple turtles can be controlled independently using separate topics.
* GitHub helps track and manage development progress effectively.

---

## Screenshots 

Include:

* Turtlesim running
* Turtle moving in patterns
* Multiple turtles spawned

---

## Conclusion

This lab provided practical experience in setting up a ROS 2 development environment and integrating it with GitHub. Creating and modifying a custom node helped in understanding how robots can be controlled programmatically using velocity commands. The experiment also demonstrated how different motion patterns can be achieved using ROS 2 topics.

---
