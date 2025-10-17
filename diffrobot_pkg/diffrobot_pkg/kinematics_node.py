# Subscribes to ticks and integrates standard diff-drive kinematics to publish a 2D pose (x, y, theta). 
# It also exposes a service to reset the pose to a user-specified state (e.g., when placing the robot at a known start pose).
# Task:
# - Subscribes to /wheel_ticks and computes pose (x, y, theta) using differential-drive kinematics.
# - Publishes custom messages Pose2DStamped.msg on /pose.
# - Offers service /reset_pose (type SetPose.srv) to set the internal pose to given (x, y, theta).

import rclpy
from rclpy.node import Node
import numpy as np
from diffrobot_interfaces.msg import WheelTicks, Pose2DStamped #custom msg from pkg
from diffrobot_interfaces.srv import SetPose #custom msg and srv message from pkg
from .robot_parameters import wheel_radius, wheel_axel_width, encoder_resolution, t #Robot's configuration

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
        super().__init__('kinematics_node') #name attribute
        # Initial Position Values
        self.x = 0
        self.y = 0
        self.theta = 0
        # Initial "past" tick counts
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

        self.WheelTicks_data_instance = None


    # SUBSCRIBER CALLBACK
    def sub_wheelticks_callback(self, msg:WheelTicks):
        # Runs everytime it recieves a msg through /wheel_ticks topic
        self.get_logger().info(
            f"The robot's wheels have rotated:" 
            f"left wheel: {msg.left_ticks} ticks, right wheel:{msg.right_ticks} ticks.") #Same as Encoder's publisher
        self.WheelTicks_data_instance = msg #Stores the recieved msg


    # PUBLISHER CALLBACK
    def pub_pose_callback(self):
        msg = Pose2DStamped()

        # Calculate the position using wheel ticks amounts:
        # Rename the data for readability
        right_ticks = self.WheelTicks_data_instance.right_ticks
        left_ticks = self.WheelTicks_data_instance.left_ticks

        # Calculate position with Diff. Drive Kinematics
        # For change between tick amounts - Robot moved
        if right_ticks != self.right_ticks_past | left_ticks != self.left_ticks_past:
            # Get difference between tick number to get Angular velocity
            # Order does matter; signifies direction of rotation (do not use magnitude)
            right_ticks_diff = right_ticks - self.right_ticks_past
            left_ticks_diff = left_ticks - self.left_ticks_past

            # Calculate linear wheel velocities:
            degrees_right = (360/encoder_resolution)*right_ticks_diff
            degrees_left = (360/encoder_resolution)*left_ticks_diff

            w_right_deg = degrees_right/t #Only with the difference
            w_left_deg = degrees_left/t #Only with the difference

            w_right = w_right_deg*(np.pi/180) #Only with the difference
            w_left = w_left_deg*(np.pi/180) #Only with the difference

            # Define Jacobian and angular velocity vector (rad/s)
            # Angular velocity vector - [phi_dotR; phi_dotL] aka omegaR and omegaL wR wL
            angular_velocity_vector = np.array([[w_right],[w_left]])

            # Jacobian
            Ja = np.array([[(wheel_radius/2)*np.cos(self.theta), (wheel_radius/2)*np.cos(self.theta)],
                        [(wheel_radius/2)*np.sin(self.theta), (wheel_radius/2)*np.sin(self.theta)],
                        [(wheel_radius/wheel_axel_width), -(wheel_radius/wheel_axel_width)]])

            # Velocity vector - [x_dot; y_dot; theta_dot] - Result
            velocity_vector = Ja @ angular_velocity_vector

            # Position vector - [x; y; theta] - Result
            position_vector = t * velocity_vector #TODO VERIFY LOGIC FOR TIME AMOUNT
            
            # Update x,y,theta values stored in attributes
            self.x = self.x + position_vector[0]
            self.y = self.y + position_vector[1]
            self.theta = self.theta + position_vector[2]

            # Write the data to the message 
            msg.x = self.x
            msg.y = self.y
            msg.theta = self.theta
    
            # Publish and Logger
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: x:%d, y:%d, theta:%d' % (msg.x, msg.y, msg.theta))

            # Store values right before next loop/msg - Naturally accumulate, no need to add
            self.right_ticks_past = right_ticks
            self.left_ticks_past = left_ticks

        elif right_ticks == self.right_ticks_past and left_ticks == self.left_ticks_past:
            # Publish and Logger
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: x:%d, y:%d, theta:%d. No change.' % (msg.x, msg.y, msg.theta)) 

        else:
            self.get_logger().info('Error')


    # SERVER CALLBACK
    def server_resetpose_callback(self, request, response):
        # Evaluate if the requested position can be Accepted or Not - NOT NECESSARY IN THIS CASE
        response.accepted = True

        # After accepted or rejected, Position Process:
        # Different logs for the different situations; if response is accepted or not.
        if response.accepted:
            self.x = request.x
            self.y = request.y
            self.theta = request.theta
            response.status = f"Current set position: [x:{self.x}, y:{self.y} ,theta:{self.theta}]" #TODO-IS THIS EVEN SEEN OR JUST REPLACED AND NOT EVEN SEEN??
            self.get_logger().info('Incoming request\n[x:%d, y:%d, theta:%d]' % (request.x, request.y, request.theta)) 
            #TODO - ASK - Can the other method be used? Fstring?

        # Current postion, if not accepted, no changes:
        elif not response.accepted:
            response.status = f"Current set position: [x:{self.x}, y:{self.y}, theta:{self.theta}]" 
            self.get_logger().info('Robot was not able to be reset. Request was NOT accepted')

        else:
            response.status = f"Current set position: [x:{self.x}, y:{self.y}, theta:{self.theta}]" 
            self.get_logger().info('Robot was not able to be reset. Error.')

        # Return the response part of the message when the function is run, with the assigned values
        return response
               
def main(args=None): #Input arguments are set to None (Classtype), arguments for ros2 parameters
    rclpy.init(args=args) #Input arguments are reset to their original values for usage. Just passed along by main()

    kinematics_node = KinematicsNode()
    rclpy.spin(kinematics_node)
    kinematics_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()