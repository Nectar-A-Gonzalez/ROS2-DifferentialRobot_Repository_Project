# Subscribes to ticks and integrates standard diff-drive kinematics to publish a 2D pose (x, y, theta). 
# It also exposes a service to reset the pose to a user-specified state (e.g., when placing the robot at a known start pose).
# Task:
# - Subscribes to /wheel_ticks and computes pose (x, y, theta) using differential-drive kinematics.
# - Publishes custom messages Pose2DStamped.msg on /pose.
# - Offers service /reset_pose (type SetPose.srv) to set the internal pose to given (x, y, theta).

import rclpy
import rclpy.Node as Node
# import numpy as np
# from geometry_msgs.msg import Twist #base ros2 installation
# from diffrobot_interfaces.msg import WheelTicks #custom pkg
# import robot_parameters #Robot's geometrical configuration

# SIMUL Input

# Wheelticks.msg
# builtin_interfaces/Time stamp
# int32 left_ticks
# int32 right_ticks

# Pose2DStamped.msg
# builtin_interfaces/Time stamp
# float32 x
# float32 y
# float32 theta

# Math - TODO - lINK Formula paper in the readme
class KinematicsNode(Node):
    def __init__(self):
        super.__init__('kinematics_node') #name attribute 
        # SUBSCRIBER TO /wheel_ticks (left tick amount, right tick amount; cummulative)
        FGG
        # PUBLISHER TO /pose (after calculating 2D pose from wheel ticks)
        SSR
        # SERVER TO /reset_pose (set pose as a desired on, #assume clear wheel tick amounts)
        HJHJ

    #SUBSCRIBER CALLBACK
    #def ()
    #PUBLISHER CALLBACK



    # Verify with values of msg before as to not be same values, since encoder is cummulative
    # If value is same as before (since this publishes on a timer not on input)

def main(ARGS=None): #Input arguments are set to None (Classtype), 
    rclpy.init(args=args) #Input arguments are reset to their original values for usage. Just passed along by main()


if __name__ == '__main__':
    main()