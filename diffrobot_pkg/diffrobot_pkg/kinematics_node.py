# Subscribes to ticks and integrates standard diff-drive kinematics to publish a 2D pose (x, y, theta). 
# It also exposes a service to reset the pose to a user-specified state (e.g., when placing the robot at a known start pose).
# Task:
# - Subscribes to /wheel_ticks and computes pose (x, y, theta) using differential-drive kinematics.
# - Publishes custom messages Pose2DStamped.msg on /pose.
# - Offers service /reset_pose (type SetPose.srv) to set the internal pose to given (x, y, theta).

import rclpy
import rclpy.Node as Node
from diffrobot_interfaces.msg import WheelTicks, Pose #custom msg from pkg
from diffrobot_interfaces.srv import SetPose #custom srv message from pkg

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
        super.__init__('kinematics_node') #name attribute 
        # SUBSCRIBER TO /wheel_ticks (left tick amount, right tick amount; cummulative)
        self.subscription = self.create_subscription(WheelTicks, 'wheel_ticks', self.sub_wheelticks_callback, 25) #msg class type,topic name, callback, reserve amount)
        
        # PUBLISHER TO /pose (after calculating 2D pose from wheel ticks)
        self.publisher_ = self.create_publisher(Pose, 'pose', 25)
        timer_period = 0.05 #seconds #Using same Hz as EncoderNode #TODO-Verify if same HZ is good idea ASK
        self.pub_timer = self.create_timer(timer_period, self.pub_pose_callback) 
        
        # SERVER TO /reset_pose (set pose as a desired on, #assume clear wheel tick amounts)
        HJHJ #TODO-THIS.

    # SUBSCRIBER CALLBACK
    def sub_wheelticks_callback(self, msg:WheelTicks):
        # Runs everytime it recieves a msg through /wheel_ticks topic
        self.get_logger().info(
            f"The robot's wheels have rotated:" 
            f"left wheel: {msg.left_ticks} ticks, right wheel:{msg.right_ticks} ticks.") #Same as Encoder's publisher
        self.WheelTicks_data_instance = msg #Stores the recieved msg #TODO-Maybe move all the loggers after code part??

    # PUBLISHER CALLBACK
    def pub_pose_callback(self):
        msg = Pose()


         #TODO-REMEMBER CALCULATE DIFFERENCE AND ONLY USE DIFFERENCE



    # Verify with values of msg before as to not be same values, since encoder is cummulative
    # If value is same as before (since this publishes on a timer not on input)



def main(args=None): #Input arguments are set to None (Classtype), arguments for ros2 parameters TODO-CHECK INFO
    rclpy.init(args=args) #Input arguments are reset to their original values for usage. Just passed along by main()
    kinematics_node = KinematicsNode()
    rclpy.spin(kinematics_node)
    kinematics_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()