# Simulates wheel enconders by publishing cumulative left/right tick counts at 20 Hz based on commanded velocities (/cmd_vel)
# Tasks:
# - Publishes custom message WheelTicks.msg on /wheel_ticks at 20 Hz.
# - Includes builtin_interfaces/Time stamps
# - Interprets /cmd_vel (geometry_msgs/Twist) to update wheel tick increments. (aka a SUBSCIRBER)
#   (You may generate your own /cmd_vel for testing; teleop is optional and not graded).

#import rclpy
#import rclpy.node as Node
#import WheelTicks.mgs as WheelTicks
#import dfdfdf
#import numpy as np

# SIMUL INPUT
# Vx - 
# Wz - 

# geoemetry/Twist structure


# WheelTicks.msg structure
# builtin_interfaces/Time stamp
# int32 left_ticks
# int32 right_ticks


# Variables for configuration:
wheel_radius = 
wheel_axel_width =
encoder_tick_amount =
ticks_per_degree =
t = #time the velocity is applied for

#### do i need to include these variables as input for them to be used?????

class EncoderNode(Node):
    
    def __init__(self):
        super.__init__
# Take Vx as robot's linear velocity and Wz as robots angular velocity
# Calculate individual linear wheel velocities (from cmd_vel Vx and Wz given values)
V_right_wheel = V_robot + w_robot * wheel_axel_width/2 #TODO Change V_robot and w_robot to the correct connected variables to the msg object 
V_left_wheel = V_robot - w_robot * wheel_axel_width/2
# Convert to angular velocities (per wheel)
w_right = V_right_wheel/wheel_radius
w_left = V_left_wheel/wheel_radius
# Convert rad/s to deg/s
w_right_deg = w_right/
w_left_deg = w_left * (180/)
# Divide by time the angular velocity is applied to get the degrees the wheel turned
degrees_right = w_right_deg/t
degrees_left = w_left_deg/t


# Calculate angular velocities per wheel
# JKJKJ
# DFGDF
# FDGFGF
# GDGF 

# one call back per channel connection

    #def

# def main()