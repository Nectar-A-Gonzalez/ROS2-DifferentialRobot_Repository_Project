# Simulates wheel enconders by publishing cumulative left/right tick counts at 20 Hz based on commanded velocities (/cmd_vel)
# Tasks:
# - Publishes custom message WheelTicks.msg on /wheel_ticks at 20 Hz.
# - Includes builtin_interfaces/Time stamps
# - Interprets /cmd_vel (geometry_msgs/Twist) to update wheel tick increments. (aka a SUBSCIRBER)
#   (You may generate your own /cmd_vel for testing; teleop is optional and not graded).

import rclpy
from rclpy.node import Node
import numpy as np
from geometry_msgs.msg import Twist #base ros2 installation
from diffrobot_interfaces.msg import WheelTicks #custom pkg

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

# Variables for configuration:
wheel_radius = we #(meters)#CHANGEABLE
wheel_axel_width = we #(meters)CHANGEABLE
encoder_tick_amount = ewe #CHANGEABLE  #TODO - CHANGE TO ACTUAL TERMINOLOGY BROSKI
ticks_per_degree = encoder_tick_amount/360
t = 1 #time the velocity is applied for #(seconds)#CHANGEABLE

#### do i need to include these variables as input for them to be used????? #TODO - Verify this 

class EncoderNode(Node): 
    def __init__(self):
        super.__init__("encoder_node") #name attribute
        # SUBSCRIBER TO /cmd_vel TOPIC - (Gets Vx and Wz)
        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.sub_cmdvel_callback, 25) #msg class type,topic name, callback, reserve amount)
        self.subscription # recommended to prevent unused variable warning

        # PUBLISHER TO /wheel_ticks TOPIC AT 20Hz (~20 times per second)
        self.publisher_ = self.create_publisher(WheelTicks, 'wheel_ticks', 25) # msg class,topic name (topic seems to be created here), allowable data reserve #FIX Research later
        timer_period = 0.05 #seconds #time interval it will publish/run the callback at #Publish 20Hz -> publish each 0.05 seconds
        self.pub_timer = self.create_timer(timer_period, self.pub_wheelticks_callback)
        self.i = 0

    def sub_cmdvel_callback(self,msg:): #Runs everytime it recieves a msg through /cmd_vel topic #FLAG
        self.get_logger().info(f'The robot currently travels:{msg.data}.') #FLAG


    def pub_wheelticks_callback(self, msg: ): 
        # Run this function every 0.05 seconds #Calculated from Twist msg recieved (aka Vx and Wz) to obtain wheel tick amount:
        msg = 

        #TODO - Figure out how the data should be shared between them I am confusion

        # Take Vx as robot's linear velocity and Wz as robots angular velocity (Change with topic publish, this goes in a callback)
        # Calculate individual linear wheel velocities (from cmd_vel Vx and Wz given values)
        V_right_wheel = V_robot + w_robot * wheel_axel_width/2 #TODO Change V_robot and w_robot to the correct connected variables to the msg object 
        V_left_wheel = V_robot - w_robot * wheel_axel_width/2 

        # Convert to angular velocities (per wheel)
        w_right = V_right_wheel/wheel_radius
        w_left = V_left_wheel/wheel_radius

        # Convert rad/s to deg/s
        w_right_deg = w_right * (180/np.pi)
        w_left_deg = w_left * (180/np.pi)

        # Divide by time the angular velocity is applied to get the degrees the wheel turned
        degrees_right = w_right_deg/t
        degrees_left = w_left_deg/t

        # Calculate the ticks the encoder has/should count - CUMULATIVE AMOUNTS
        right_ticks = sed #TODO Change to msg object variables
        left_ticks = sd #TODO Change to msg object variables

# only calculate when callback called, but how do i make it cummulative? 


# one call back per channel connection

    #def

# def main()