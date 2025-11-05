# DiffRobot_pkg
These packages are used to model a differential drive robot that communicates via ROS2 - Jazzy Distro.
The diffrobot_pkg includes the three nodes that are used to simulate the differential robots behavior.
The behavior is as follows:<br>
- The robot is given a velocity at which it should move, the encoders are simulated through a node, which takes that linear and angular velocity (Vx and wz) and translates it into the amount of ticks the encoder would read, if the velocity is applied for 1 (one) second and the encoder has a resolution of dfddfdfdf (variables defined in the robot_parameters.py, change for your use case).<br>
- Based on the amount of ticks read by the encoders and if they changed from the previous instance, the new position of the robot is calculated.<br>
dfdfd
- The encoders "read" the angular velocity of each wheel in terms of tics read per degree dfdfererer
 
> [!Note] 
> The instructions given here are for a Linux OS.<br>
> Package is for ROS2 - Jazzy <br>
> They assume ROS2 already installed and sourced in the terminals.<br>

#Communicates to what Explain the ros way of communicating or just the data processing aspect, I think only the logical part #IDEA
#And maybe give instrutions to how to see ros communication nodes relationships. #IDEA

## How to build the package in your own workspace:
To build the package in a workspace, you first need to create your workspace folder (if you don't already have one).<br>

### Create a workspace
To do that, in a terminal window write:

    mkdir -p ~/YOUR-WORKSPACE/src 
    cd ~/YOUR-WORKSPACE/src

This creates a folder with the name you decide for your workspace, and creates a folder called `src` inside of it.<br>
It then positions you inside the `src` folder, where your packages will be downloaded to; along with any source code you will use in your project.

### Download the packages
While inside the `src` folder, clone this repository to the folder:

    git clone https://github.com/Nectar-A-Gonzalez/ROS2-DifferentialRobot_Repository_Project

Here the diffrobot_pkg hold the dfdfdffdf code, while diffrobot_interfaces holds the necessary msg and srv templates for ROS2 communication.

### Resolve Dependencies
Before we can _build_ the workspace, we need to check if all the required package dependencies are installed.<br>
Go to the root of your workspace
    
    cd ~/YOUR-WORKSPACE/

Check the dependencies:

    rosdep install -i --from-path src --rosdistro jazzy -y
    # Output: All required rosdeps installed sucessfully

### Build the workspace
Finally, we can build the workspace
From the root of your workspace, run:
    
    colcon build
    # Output:
    # Starting >>> ####
    # Finished <<< #### [###]
    # Summary: 2 package finished [###]

## How to source and run the package
To be able to access the executables that were just built in our current terminal, we need to source them:

    source install/setup.bash

## Commands to test the pub/sub and service/client communications:
sdsdsdsd<br>

Verify 



To simulate a commanding velocity input, dfdf<br>

    ros2 pub dfdfdf at -rate 10
    dfd
    klklkl

dfdfdf<br>

    df
    dfdf

## Required Verification
### 0 Create a new workspace, build and source:<br>

Create the new workspace:<br>
```
mkdir -p ~/YOUR-WORKSPACE/src && cd ~/YOUR-WORKSPACE/src
```

Clone the Repository INSIDE the src folder:<br>
```
git clone https://github.com/Nectar-A-Gonzalez/ROS2-DifferentialRobot_Repository_Project.git
```

Move back to the root of the workspace to verify dependencies and build:<br>
```
cd ../
```
```
rosdep install -i --from-path src --rosdistro jazzy -y
```
```
colcon build
```

Source the code in the current terminal (necessary for each new terminal):<br>
```
source install/setup.bash
```

### 1 Interfaces exist and are introspectable:<br>
```
ros2 interface show diffrobot_interfaces/msg/WheelTicks
ros2 interface show diffrobot_interfaces/msg/Pose2DStamped
ros2 interface show diffrobot_interfaces/srv/SetPose
```

### 2 Launch stack (encoder + kinematics):
```
ros2 launch diffrobot_pkg diffrobot_launch.py
```

### 3 Topics appear and produce data:
```
ros2 topic list | grep -E '^/wheel_ticks$|^/pose$'
ros2 topic echo /wheel_ticks --once
ros2 topic echo /pose --once
```


### 4 Publish a test velocity for at least 3 seconds:<br>
Since this package does not have an auto-publishing node for the cmd-vel topic, it is necessary to manually publish velocities to the topic.<br>
In another terminal after sourcing, run:
```
ros2 topic pub /cmd_vel geometry_msgs/Twist "{linear: {x: 0.2, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}" -r 10
```

### 5 Verify pose changes over time (run twice a few seconds apart)
```
ros2 topic echo /pose --once
sleep 2
ros2 topic echo /pose --once
```

### 6 Service exists with correct type
```
ros2 service type /reset_pose
# Expected output: diffrobot_pkg/srv/SetPose
```

### 7 Call service directly via CLI
```
ros2 service call /reset_pose diffrobot_pkg/srv/SetPose "{x: 1.0, y: 0.0, theta: 1.57}"
```

### 8 Call service using your client node
```
ros2 run diffrobot_pkg reset_client -- --x 0.0 --y 0.0 --theta 0.0 #THIS SEEMS WEIRD BTW
```


## Example Outputs Video - Using the test commands


### Some References:<br>
[Differential Drive Kinematics Notes by The University of Columbia](https://www.cs.columbia.edu/~allen/F17/NOTES/icckinematics.pdf "CS W4733 NOTES - Differential Drive Robots")<br>
[Kinematics of Differential Drive Robots and Odometry Video by Engineering Educator Academy](https://www.youtube.com/watch?v=RZlZcDxQ8P4 "Kinematics of Differential Drive Robots and Odometry")<br>
[5.2. Motion Model for the Differential Drive Robot from "Introduction to Robotics and Perception" from Georgia Tech](https://www.roboticsbook.org/S52_diffdrive_actions.html "5.2. Motion Model for the Differential Drive Robo")<br>


inside the repository folder/ repository folder as current working directory
git fetch https://Nectar-A-Gonzalez/
git pull

Vector variables are lists, so to get x, y, z, you need to use list indexing NOT atribute indexing or maybe you do? but x directly?
TODO - VERIFY THERE IS NO OTHER WAY If you make it a list IT WONT WORK #Needs to be assigned INDIVIDUALLY
git pull https://github.com/Nectar-A-Gonzalez/ROS2-DifferentialRobot_Repository_Project.git