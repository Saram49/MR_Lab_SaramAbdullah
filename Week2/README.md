# Week 2 – ROS 2 Topics, Services, and Turtlesim

## Overview

This lab focuses on understanding core ROS 2 communication mechanisms including **topics and services** using the **Turtlesim simulator**. The objective is to gain hands-on experience with ROS 2 CLI tools and visualize interactions between nodes in a simulated environment.

---

## Objectives

* Learn ROS 2 command-line tools (CLI)
* Understand topics and message flow
* Understand services and request-response behavior
* Control a simulated robot using Turtlesim
* Explore ROS 2 graph using `rqt`

---

## Prerequisites

Before performing this lab:

* ROS 2 Humble must be installed
* Basic Linux commands knowledge
* Understanding of:

  * Nodes
  * Topics
  * Services

---

## Tools Used

* ROS 2 Humble
* Turtlesim package
* rqt (GUI tool)
* Ubuntu Linux

---

## Important Commands

### Source ROS 2

```bash id="c1"
source /opt/ros/humble/setup.bash
```

### Install Turtlesim (if not installed)

```bash id="c2"
sudo apt install ros-humble-turtlesim
```

### Run Turtlesim Node

```bash id="c3"
ros2 run turtlesim turtlesim_node
```

### Control Turtle (Keyboard)

```bash id="c4"
ros2 run turtlesim turtle_teleop_key
```

### List Topics

```bash id="c5"
ros2 topic list
```

### View Topic Data

```bash id="c6"
ros2 topic echo /turtle1/pose
```

### Publish Velocity Command

```bash id="c7"
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {z: 1.8}}"
```

### Call Reset Service

```bash id="c8"
ros2 service call /reset std_srvs/srv/Empty
```

### Open RQT GUI

```bash id="c9"
rqt
```

---

## Procedure Summary

1. Launched the Turtlesim simulation using ROS 2.
2. Controlled the turtle using keyboard teleoperation.
3. Observed active topics and monitored turtle position.
4. Published velocity commands to control movement.
5. Used ROS 2 services to reset the simulation.
6. Explored the system using `rqt` GUI.
7. Spawned a second turtle and controlled it independently.

---

## Observations

* Topics allow continuous data flow between nodes (e.g., position updates).
* Services provide instant request-response functionality (e.g., reset).
* Multiple nodes can run simultaneously and interact through ROS 2 communication.
* `rqt` provides a graphical way to visualize nodes, topics, and services.

---

## Screenshots (to be added)

Include the following:

* Turtlesim window running
* Teleoperation control
* `ros2 topic list`
* `ros2 topic echo`
* `rqt` interface
* Service calls (`/reset`, `/spawn`)
* Two turtles in simulation

---

## Conclusion

This lab provided a clear understanding of ROS 2 communication using topics and services. The Turtlesim simulator helped visualize how commands affect robot behavior in real time. The use of `rqt` made it easier to analyze the interaction between nodes, topics, and services.

---
