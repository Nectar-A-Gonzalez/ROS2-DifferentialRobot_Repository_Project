# Subscribes to ticks and integrates standard diff-drive kinematics to publish a 2D pose (x, y, theta). 
# It also exposes a service to reset the pose to a user-specified state (e.g., when placing the robot at a known start pose).
# Task:
# - Subscribes to /wheel_ticks and computes pose (x, y, theta) using differential-drive kinematics.
# - Publishes custom messages Pose2DStamped.msg on /pose.
# - Offers service /reset_pose (type SetPose.srv) to set the internal pose to given (x, y, theta).

import rclpy
import rclpy.Node as Node
import numpy as np
from diffrobot_interfaces.msg import WheelTicks, Pose #custom msg from pkg
from diffrobot_interfaces.srv import Pose2DStamped, SetPose #custom msg and srv message from pkg
from robot_parameters import wheel_radius, wheel_axel_width, encoder_resolution, t #Robot's configuration

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
        # Create position attributes and initialize at position and angle 0
        # Robot's current position attribute 
        self.x = 0
        self.y = 0
        self.theta = 0
        # Initial "past" tick values
        self.right_ticks_past = 0
        self.left_ticks_past = 0

        # SUBSCRIBER TO /wheel_ticks (left tick amount, right tick amount; cummulative)
        self.subscription = self.create_subscription(WheelTicks, 'wheel_ticks', self.sub_wheelticks_callback, 25) #msg class type,topic name, callback, reserve amount)
        
        # PUBLISHER TO /pose (after calculating 2D pose from wheel ticks)
        self.publisher_ = self.create_publisher(Pose2DStamped, 'pose', 25)
        timer_period = 0.05 #seconds #Using same Hz as EncoderNode # TODO-Verify if same HZ is good idea ASK
        self.pub_timer = self.create_timer(timer_period, self.pub_pose_callback) 
        
        # SERVER TO /reset_pose (set pose as a desired on, #assume clear wheel tick amounts)
        self.srv = self.create_service(SetPose,"reset_pose", self.server_resetpose_callback)
        #Uses reset pose srv message type - Remember uses a SERVICE CHANNEL NOT A TOPIC CHANNEL


    # SUBSCRIBER CALLBACK
    def sub_wheelticks_callback(self, msg:WheelTicks):
        # Runs everytime it recieves a msg through /wheel_ticks topic
        self.get_logger().info(
            f"The robot's wheels have rotated:" 
            f"left wheel: {msg.left_ticks} ticks, right wheel:{msg.right_ticks} ticks.") #Same as Encoder's publisher
        self.WheelTicks_data_instance = msg #Stores the recieved msg # TODO-Maybe move all the loggers after code part??


    # PUBLISHER CALLBACK
    def pub_pose_callback(self):
        msg = Pose2DStamped()

        # Calculate the position using wheel ticks amounts:
        # Rename the data for readability
        right_ticks = self.WheelTicks_data_instance.right_ticks
        left_ticks = self.WheelTicks_data_instance.left_ticks

        # Calculate linear wheel velocities: # TODO-Verify if actually use linear velocities??
        degrees_right = (360/encoder_resolution)*right_ticks
        degrees_left = (360/encoder_resolution)*left_ticks

        w_right_deg = degrees_right/t 
        w_left_deg = degrees_left/t

        w_right = w_right_deg*(np.pi/180)
        w_left = w_left_deg*(np.pi/180)

        # V_right_wheel = w_right*wheel_radius
        # V_left_wheel = w_left*wheel_radius

        

        # Calculate position with Diff. Drive Kinematics
        
        #TODO-REMEMBER CALCULATE DIFFERENCE AND ONLY USE DIFFERENCE
        if 

        elif 



        # Calculate position - only for when wheel ticks change well actually? # TODO-Figure this out

        # you get the velocity but umm? uhhh velocity could be well umm? # TODO-Figure this out
        #if 

        # Verify with values of msg before as to not be same values, since encoder is cummulative #TODO-Figure out math first to see if this is even necesary
        # If value is same as before (since this publishes on a timer not on input)

        # Store calculated current position in self attribute

        # Publish and Store to logger

        #Store last value for tick in old, for next message


    # SERVER CALLBACK
    def server_resetpose_callback(self, request, response):
        #Execute the service and give response values:
        # Take clients request and apply to the self current position attribute #TODO-VERIFY IF CORRECT
        x_new = request.x
        y_new = request.y
        theta_new = request.theta
        #Apply to current position attribute
        self.current_position[0] = x_new
        self.current_position[1] = y_new
        self.current_position[2] = theta_new

        # Establish response srv values for the message # TODO-VERIFY IF CORRECT 
        # Si requested position is actually posible or not
        response.accepted = dfdf
        #Current postion, if not accepted, no changes.
        response.status = f"Requested position: {KK}, Final position: {IKK}"
# SEE IF THERE IS A PUBLISH OR SIMILAR COMMAND #TODO
 
 
               
def main(args=None): #Input arguments are set to None (Classtype), arguments for ros2 parameters #TODO-CHECK INFO
    rclpy.init(args=args) #Input arguments are reset to their original values for usage. Just passed along by main()
    kinematics_node = KinematicsNode()
    rclpy.spin(kinematics_node)
    kinematics_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()