# Week 1 – Post Lab Answers

## 1. Definitions

**Node**
A node is a single executable process in ROS 2 that performs a specific task such as controlling hardware, processing sensor data, or running an algorithm.

**Topic**
A topic is a named communication channel used by ROS 2 nodes to send and receive messages asynchronously.

**Package**
A package is a structured folder that contains ROS 2 source code, dependencies, configuration files, and build instructions.

**Workspace**
A workspace is a directory that contains one or more ROS 2 packages along with build, install, and log files.

---

## 2. Why sourcing is required

Sourcing a workspace loads the required ROS 2 environment variables so the system can locate packages, executables, and dependencies.
If the workspace is not sourced, ROS 2 will not detect the packages in that workspace and commands like `ros2 run` or `ros2 pkg list` will fail.

---

## 3. Purpose of `colcon build`

`colcon build` is used to compile and build all ROS 2 packages inside a workspace.

It generates the following folders:

* **build/** – contains intermediate compilation files
* **install/** – contains installed packages and executables used by ROS 2
* **log/** – contains logs of the build process

---

## 4. Entry points console script in `setup.py`

The `entry_points` section in `setup.py` registers a Python function as a command-line executable.
This allows ROS 2 to run the node using the command:

`ros2 run <package_name> <executable_name>`

It maps the executable name to the Python file and function that should run.

Example:

```
simple_node = my_first_pkg.simple_node:main
```

This tells ROS 2 to run the `main()` function inside `simple_node.py`.

---

## 5. Publisher–Subscriber Diagram

```
+-------------------+        /example_topic        +-------------------+
|    Publisher      | ----------------------------> |    Subscriber     |
|       Node        |                               |       Node        |
|                   |                               |                   |
|  Publishes data   |                               |   Receives data   |
+-------------------+                               +-------------------+
```
