# Simulates wheel enconders by publishing cumulative left/right tick counts at 20 Hz based on commanded velocities (/cmd_vel)
# Tasks:
# - Publishes custom message WheelTicks.msg on /wheel_ticks at 20 Hz.
# - Includes builtin_interfaces/Time stamps
# - Interprets /cmd_vel (geometry_msgs/Twist) to update wheel tick increments. (aka a SUBSCIRBER)
#   (You may generate your own /cmd_vel for testing; teleop is optional and not graded).

import rclpy #I assume rclpy is part of base ROS2 installation and that is why it is accesable and do not have to do pip
from rclpy.node import Node
import numpy as np
from geometry_msgs.msg import Twist #base ros2 installation
from diffrobot_interfaces.msg import WheelTicks #custom msg from pkg
from robot_parameters import wheel_radius, wheel_axel_width, encoder_resolution, t #Robot's configuration

# SIMUL INPUT
# Vx - (meters/second)
# Wz - (radians/second)

# geoemetry/Twist structure:
# Vector3 linear
#    float64 x
#    float64 y
#    float64 z
# Vector3 angular
#    float64 x
#    float64 y
#    float64 z

# WheelTicks.msg structure:
# builtin_interfaces/Time stamp
# int32 left_ticks
# int32 right_ticks

class EncoderNode(Node): 
    def __init__(self):
        super.__init__("encoder_node") #name attribute
        # SUBSCRIBER TO /cmd_vel TOPIC - (Gets Vx and Wz)
        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.sub_cmdvel_callback, 25) #msg class type,topic name, callback, reserve amount)
        self.subscription # recommended to prevent unused variable warning

        # PUBLISHER TO /wheel_ticks TOPIC AT 20Hz (~20 times per second)
        self.publisher_ = self.create_publisher(WheelTicks, 'wheel_ticks', 25) # msg class,topic name (topic seems to be created here), allowable data reserve #TODO - Research later
        timer_period = 0.05 #seconds #time interval it will publish/run the callback at #Publish 20Hz -> publish each 0.05 seconds
        self.pub_timer = self.create_timer(timer_period, self.pub_wheelticks_callback)         
    

    def sub_cmdvel_callback(self,msg:Twist):
        # Runs everytime it recieves a msg through /cmd_vel topic #TODO-FLAG
        self.get_logger().info(f'The robot currently travels:{msg.linear.x} m/s and {msg.angular.z}rad/s') #TODO-FLAG
        # Stored message into attribute so they are accesible for the publisher # Attribute created at method run
        self.Twist_data_instance = msg

    
    def pub_wheelticks_callback(self):
        msg = WheelTicks()
        # Run this function every 0.05 seconds #Calculated from Twist msg recieved (aka Vx and Wz) to obtain wheel tick amount:
        V_robot = self.Twist_data_instance.linear.x #Robot's linear velocity Vx (linear_x)
        w_robot = self.Twist_data_instance.angular.z #Robot's angular velocity Wz (angular_z)

        # CALCULATIONS:
        # Take Vx as robot's linear velocity and Wz as robots angular velocity (Change with topic publish, this goes in a callback)
        # Calculate individual linear wheel velocities (from cmd_vel Vx and Wz given values)
        V_right_wheel = V_robot + w_robot * wheel_axel_width/2
        V_left_wheel = V_robot - w_robot * wheel_axel_width/2 

        # Convert to angular velocities (per wheel)
        w_right = V_right_wheel/wheel_radius
        w_left = V_left_wheel/wheel_radius

        # Convert rad/s to deg/s
        w_right_deg = w_right * (180/np.pi)
        w_left_deg = w_left * (180/np.pi)

        # Divide by time the angular velocity is applied to get the degrees the wheel turned
        degrees_right = w_right_deg*t #TODO-VERIFY CORRECTION (from w/t to w*t)
        degrees_left = w_left_deg*t

        # Calculate the ticks the encoder has/should count - CUMULATIVE AMOUNTS 
        # Also pass values to msg attributes in one go
        msg.right_ticks = (encoder_resolution/360)*degrees_right #Pulses per rotation/360 * degrees wheel rotated due to speed
        msg.left_ticks = (encoder_resolution/360)*degrees_left

        # Publish msg data established to topic
        self.publisher_.publish(msg)
        # Store msg data in Node's logger - Made one line just in case it doesnot support multiline logs
        self.get_logger().info(
            f"The robot's wheels have rotated:" 
            f"left wheel: {msg.left_ticks} ticks, right wheel:{msg.right_ticks} ticks.")
        


def main(args=None):
    rclpy.init(args=args) #Initiate

    encoder_node = EncoderNode() #Establish attribute Node name as varible for Node object
    rclpy.spin(encoder_node)

    # Destroy the node explicitly
    # (optional... will be done automatically)
    encoder_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()