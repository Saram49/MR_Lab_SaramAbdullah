from launch import LaunchDescription
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
            package='my_turtle_package',
            executable='move2_turtle',
            name='sim',
            output='screen'
         ),
        
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop',
            output='screen',
            prefix='xterm -e'
        )
        
        
    ])
