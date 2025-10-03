# Robot's configuration:
# Variables for configuration (CHANGEABLE): #TODO-MENTION THIS IN THE README and give the test values
# These do not vary from velocity command to velocity command
wheel_radius = 0.0889 #(meters) 
wheel_axel_width = 0.2032 #(meters)
encoder_resolution = 500 #Pulses per Rotation PPR
t = 1 #(seconds) #time the velocity is applied for

#Future improvements - these as parameters for
#the launch file might be recommended. So that they
#be changed directly from the command line and all nodes
#still use the same values. 
#https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Launch/Using-ROS2-Launch-For-Large-Projects.html