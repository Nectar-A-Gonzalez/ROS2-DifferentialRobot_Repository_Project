# Subscribes to ticks and integrates standard diff-drive kinematics to publish a 2D pose (x, y, theta). 
# It also exposes a service to reset the pose to a user-specified state (e.g., when placing the robot at a known start pose).
# Task:
# - Subscribes to /wheel_ticks and computes pose (x, y, theta) using differential-drive kinematics.
# - Publishes custom messages Pose2DStamped.msg on /pose.
# - Offers service /reset_pose (type SetPose.srv) to set the internal pose to given (x, y, theta).
import rclpy
import rclpy.Node

class Kinematics_Node(Node ):
    # Subscrigbes to 
    # Calculates pose
    # Publishes to 
    # Service
def main(ARGS=None): #THIS INPUT CFHANGES EVERYSINGLE EFFING TIME WHAT THE HECK IS IT SUPPOSED TO DAMN BE BRO???????


if __name__ == '__main__':
    main()