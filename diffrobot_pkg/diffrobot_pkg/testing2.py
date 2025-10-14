
from robot_parameters import wheel_radius, wheel_axel_width, encoder_resolution, t #Robot's configuration
import numpy as np
#So you dont have to use nested names that usually happen with just import, like numpy 
# though i guess only use with small things (numpy is a heck of a library)

wheel_radius = 0.1
wheel_axel_width = 0.5
t = 1

#Kinematics node
#Inputs
# Start Position
x = 0
y = 0
theta = 0
# Initialize stored tick values, first comparision
right_ticks_past =
right_ticks_past = 

# Calculate the position using wheel ticks amounts:
# Rename the data for readability
# Current accumulate value
right_ticks = 100
left_ticks = 100

# Calculate linear wheel velocities: # TODO-Verify if actually use linear velocities??
degrees_right = (360/encoder_resolution)*right_ticks
degrees_left = (360/encoder_resolution)*left_ticks

w_right_deg = degrees_right/t 
w_left_deg = degrees_left/t

w_right = w_right_deg*(np.pi/180)
w_left = w_left_deg*(np.pi/180)

w_right = 240 * (2*np.pi/60)
w_left = 120 * (2*np.pi/60)


w_right = 2.75 
w_left = 1.25


# Calculate position with Diff. Drive Kinematics
# Write test logic first and THEN see if difference is necessary

# Define Jacobian and angular velocity vector (rad/s)
# Angular velocity vector - [phi_dotR; phi_dotL] aka omegaR and omegaL wR wL
angular_velocity_vector = np.array([[w_right],[w_left]])

# Jacobian
Ja = np.array([[(wheel_radius/2)*np.cos(theta), (wheel_radius/2)*np.cos(theta)],
              [(wheel_radius/2)*np.sin(theta), (wheel_radius/2)*np.sin(theta)],
              [(wheel_radius/wheel_axel_width), -(wheel_radius/wheel_axel_width)]])

# Velocity vector - [x_dot; y_dot; theta_dot] - Result
velocity_vector = Ja@angular_velocity_vector
print(velocity_vector)

pose_change = t * velocity_vector
x_new= x + pose_change[0]
y_new = y + pose_change[1]
theta_new = theta + pose_change[2]
vx = (velocity_vector[0])**2
vy = (velocity_vector[1])
2
vel_linear_mag = np.sqrt(vx,vy)
angular_robot = velocity_vector[2]
print(vel_linear_mag,angular_robot)
#TODO-REMEMBER CALCULATE DIFFERENCE AND ONLY USE DIFFERENCE



# Calculate position - only for when wheel ticks change well actually? # TODO-Figure this out

# you get the velocity but umm? uhhh velocity could be well umm? # TODO-Figure this out
#if 

# Verify with values of msg before as to not be same values, since encoder is cummulative #TODO-Figure out math first to see if this is even necesary
# If value is same as before (since this publishes on a timer not on input)

# Store calculated current position in self attribut


v1 = np.array([2,-3,0,4])
v2 = np.array([[2],[4],[5],[-3]])
multi_product = np.multiply(v1,v2)
matmul_product = np.matmul(v1,v2)
dot_product = np.dot(v1,v2)
aroba_product = v1@v2
asterisk_product = v1*v2
print(f"Multi \n{multi_product}\n" #Element by element NOT Matrix Normal (Matrix have to be same size or 1 number to all)
      f"Matmul {matmul_product}\n"
      f"Dot {dot_product}\n"
      f"Aroba {aroba_product}\n"
      f"Asterisk * \n{asterisk_product}") #Element by element NOT Matrix normal (Have to be same size or 1 number to all)

v1 = np.array([[4,2,4],[8,3,1]])
v2 = np.array([[3,5],[2,8],[7,9]])
multi_product = np.multiply(v1,v2)
matmul_product = np.matmul(v1,v2)
dot_product = np.dot(v1,v2)
aroba_product = v1@v2
asterisk_product = v1*v2
print(f"Multi \n{multi_product}\n" #Element by element NOT Matrix Normal
      f"Matmul \n{matmul_product}\n" #Matrix multiplication
      f"Dot \n{dot_product}\n" #Matrix multiplication
      f"Aroba \n{aroba_product}\n" #Matrix multiplication
      f"Asterisk * \n{asterisk_product}") #Element by element NOT Matrix normal