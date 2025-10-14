#Testing Math Logic Accuracy
#------TEST CASE-------
# Given Values
#   Wheel radius: 0.05m
#   wheelbase width: 0.30m
#   Vrobot: 1.0m/s
#   wrobot: 0.5rad/s
# Desired outputs
#   Vl = 
#   Vr = 

import numpy as np

wheel_radius = 0.05 #(meters) 
wheel_axel_width = 0.30 #(meters)
encoder_resolution = 500 #Pulses per Rotation PPR
t = 1 #(seconds) #time the velocity is applied for

# Input case values
V_robot = 1.0 #m/s #Robot's linear velocity Vx (linear_x)
w_robot = 0.5 #rad/s #Robot's angular velocity Wz (angular_z)

# CALCULATIONS:
# Take Vx as robot's linear velocity and Wz as robots angular velocity (Change with topic publish, this goes in a callback)
# Calculate individual linear wheel velocities (from cmd_vel Vx and Wz given values)
V_right_wheel = V_robot + (w_robot * wheel_axel_width/2)
V_left_wheel = V_robot - (w_robot * wheel_axel_width/2) 

# Convert to angular velocities (per wheel)
w_right = V_right_wheel/wheel_radius
w_left = V_left_wheel/wheel_radius

# Convert rad/s to deg/s
w_right_deg = w_right * (180/np.pi)
w_left_deg = w_left * (180/np.pi)

# Divide by time the angular velocity is applied to get the degrees the wheel turned
degrees_right = w_right_deg*t # TODO-VERIFY CORRECTION (from w/t to w*t)
degrees_left = w_left_deg*t

# Calculate the ticks the encoder has/should count - CUMULATIVE AMOUNTS 
# Also pass values to msg attributes in one go
right_ticks = (encoder_resolution/360)*degrees_right #Pulses per rotation/360 * degrees wheel rotated due to speed
left_ticks = (encoder_resolution/360)*degrees_left

print(f"Vr: {V_right_wheel} m/s")
print(f"Vl: {V_left_wheel} m/s")

print(f"wr: {w_right} rads/s")
print(f"wl: {w_left} rads/s")

print(f"Revs/s Right: {right_ticks/encoder_resolution} rev/s")
print(f"Revs/s Left: {left_ticks/encoder_resolution} rev/s")
print(1+((0.5*0.30)/2))
print(1+(0.5*0.30)/2)
print(1+ 0.5*0.30/2)

#----------------------------------------
# From file kinematicsnode.py 
# Calculate linear wheel velocities: # TODO-Verify if actually use linear velocities??
degrees_right = (360/encoder_resolution)*right_ticks
degrees_left = (360/encoder_resolution)*left_ticks

w_right_deg = degrees_right/t 
w_left_deg = degrees_left/t

w_right = w_right_deg*(np.pi/180)
w_left = w_left_deg*(np.pi/180)

# V_right_wheel = w_right*wheel_radius
# V_left_wheel = w_left*wheel_radius
