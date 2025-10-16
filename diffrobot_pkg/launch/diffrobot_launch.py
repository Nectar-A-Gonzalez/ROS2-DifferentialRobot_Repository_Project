# Launch File For Starting up the Necessary Nodes and potentially input variables
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='diffrobot_pkg',
            executable='encoder_node',
            name='custom_encoder_node',
            output='screen',
            emulate_tty=True,
        ),
        Node(
            package='diffrobot_pkg',
            executable='kinematics_node',
            name='custom_kinematics_node',
            output='screen',
            emulate_tty=True,
        ),
    ])
#TODO Unsure if it needs to also run reset client?