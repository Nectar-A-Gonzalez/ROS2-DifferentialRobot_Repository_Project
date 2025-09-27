# Subscribes to ticks and integrates standard diff-drive kinematics to publish a 2D pose (x, y, theta). 
# It also exposes a service to reset the pose to a user-specified state (e.g., when placing the robot at a known start pose).
# Task:
# - Subscribes to /wheel_ticks and computes pose (x, y, theta) using differential-drive kinematics.
# - Publishes custom messages Pose2DStamped.msg on /pose.
# - Offers service /reset_pose (type SetPose.srv) to set the internal pose to given (x, y, theta).

import rclpy
import rclpy.Node as Node
from 

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


class KinematicsNode(Node):
    def __init__(self):
        super.__init__()
        # SUBSCRIBER TO /wheel_ticks (left tick amount, right tick amount; cummulative)
        # PUBLISHER TO /pose (after calculating 2D pose from wheel ticks)
        # SERVER TO /reset_pose (set pose as a desired on, #assume clear wheel tick amounts)


def main(ARGS=None): #THIS INPUT CFHANGES EVERYSINGLE EFFING TIME WHAT THE HECK IS IT SUPPOSED TO DAMN BE BRO???????
    rclpy.init(args=args)
    

if __name__ == '__main__':
    main()