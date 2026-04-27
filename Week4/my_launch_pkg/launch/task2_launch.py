from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([

        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
            output='screen'
        ),

        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop',
            output='screen',
            prefix='xterm -e'
        ),
        
        # Spawn turtle2 via service call (Humble has no turtlesim 'spawn' executable).
        TimerAction(
            period=1.0,
            actions=[
                ExecuteProcess(
                    cmd=[
                        'ros2', 'service', 'call', '/spawn', 'turtlesim/srv/Spawn',
                        '{x: 3.0, y: 5.5, theta: 0.0, name: "turtle2"}'
                    ],
                    output='screen'
                )
            ]
        ),

        # Follower node - makes turtle2 follow turtle1
        Node(
            package='my_launch_pkg',
            executable='follower_node',
            name='turtle_follower',
            output='screen'
        ),

    ])
