# DiffRobot_pkg
These packages are used to model a differential drive robot that communicates via ROS2 - Jazzy Distro.
The diffrobot_pkg includes the three nodes that are used to simulate the differential robots behavior.
The behavior is as follows:<br>
- The robot is given a velocity at which it should move, the encoders are simulated through a node, which takes that linear and angular velocity (Vx and wz) and translates it into the amount of ticks the encoder would read.
- Based on the amount of ticks read by the encoders and if they changed from the previous instance, the new position of the robot is calculated.
Note: The robot's parameters are defined in the robot_parameters.py, change for your use case if necessary, but verify if functional.
<br>

> [!Note] 
> The instructions given here are for a Linux OS.<br>
> Package is for ROS2 - Jazzy <br>
> It has not been tested for other distros <br>
> They assume ROS2 is already installed and sourced in the terminals.<br>

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

Here the diffrobot_pkg holds the actual code, while diffrobot_interfaces holds the necessary msg and srv templates for ROS2 communication.

### Resolve Dependencies
Before we can _build_ the workspace, we need to check if all the required package dependencies are installed.<br>
Go to the root of your workspace:
    
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

### How to source and run the package
To be able to access the executables that we just built in our current terminal, we need to source them:

    source install/setup.bash
>[!Note]
>You need to be inside the workspace, in the `root`, to be able to source the packages.

## Run the Code Commands to test the pub/sub and service/client communications:
To efficiently start the necesary nodes, run the launch file. This will run the kinematics_node and the encoder_node.
In a sourced terminal, run the following:<br>
```
ros2 launch diffrobot_pkg diffrobot_launch.py
```
At this moment, a lot of text will appear in the terminal, it just states the robots current position (x,y,theta) for the Kinematics node and the current wheel ticks count per wheel for the Encoder node. The values should say zero, since nothing is being read, nor any velocity is being simulated for the robot.

[In new, sourced terminal] To simulate a command velocity input (the robots's simulated moving velocity), run, with the desired values<br>

    ros2 topic pub /cmd_vel geometry_msgs/Twist "{linear: {x: 0.2, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}" -r 10
(Due to the nature of the robot, movement in the z axis would not be accurate).

>[!NOTE]
>Everytime you want to run a command, relating to this package, in a new terminal, it is necessary to run the 'source command' in that terminal.]

This will publish a linear velocity of 0.2 m/s, in the direction of x, to the /cmd_vel topic. It will publish continuosly at a rate of 0.1 second times.

[In new, sourced terminal] To see the change in position for the robot, run :<br>

    ros2 topic echo /pose
[In new, sourced terminal] To reset the position of the robot to a desired position, run either of the following, with the desired positional values:<br>

    ros2 run diffrobot_pkg reset_client -- 0.0 0.0 0.0
    ros2 service call /reset_pose diffrobot_interfaces/srv/SetPose "{x: 1.0, y: 0.0, theta: 1.57}"
---
If you want to run individual nodes instead of the launch file, in a new, sourced terminal, run:

    ros2 run diffrobot_pkg kinematic_node 
This would run the kinematics node

And in another run:

    ros2 run diffrobot_pkg encoder_node 
This would run the encoder node. 
---

## Required Verification
To test the publisher and subscriber communication is working correctly.<br>
### 0 Create a new workspace, build and source:<br>
Create the new workspace:<br>
```
mkdir -p ~/YOUR-WORKSPACE/src && cd ~/YOUR-WORKSPACE/src
```

Clone the Repository INSIDE the src folder:<br>
```
git clone https://github.com/Nectar-A-Gonzalez/ROS2-DifferentialRobot_Repository_Project.git
```

Move back to the root of the workspace to verify dependencies and then build the packages:<br>
```
cd ../
```
```
rosdep install -i --from-path src --rosdistro jazzy -y
```
```
colcon build
```
>[!Note] 
>Always build in the ROOT of your workspace, not inside a subfolder.

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
# Expected output: diffrobot_interfaces/srv/SetPose 
```

### 7 Call service directly via CLI
```
ros2 service call /reset_pose diffrobot_interfaces/srv/SetPose "{x: 1.0, y: 0.0, theta: 1.57}"
```

### 8 Call service using your client node
```
ros2 run diffrobot_pkg reset_client -- --x 0.0 --y 0.0 --theta 0.0 #THIS SEEMS WEIRD BTW
ros2 run diffrobot_pkg reset_client -- 0.0 0.0 0.0
```

## Example Outputs Video - Using the test commands


### Some References:<br>
[Differential Drive Kinematics Notes by The University of Columbia](https://www.cs.columbia.edu/~allen/F17/NOTES/icckinematics.pdf "CS W4733 NOTES - Differential Drive Robots")<br>
[Kinematics of Differential Drive Robots and Odometry Video by Engineering Educator Academy](https://www.youtube.com/watch?v=RZlZcDxQ8P4 "Kinematics of Differential Drive Robots and Odometry")<br>
[5.2. Motion Model for the Differential Drive Robot from "Introduction to Robotics and Perception" from Georgia Tech](https://www.roboticsbook.org/S52_diffdrive_actions.html "5.2. Motion Model for the Differential Drive Robo")<br>

<<<<<<< HEAD
[dfdfdffdfdf](C:\Users\necam\OneDrive\1 Projects\ROS2-DifferentialRobot_Repository_Project\Assets (For README)\recordingdiffrobot_pkg.mp4)

Assets (For README)\recordingdiffrobot_pkg.mp4
C:\Users\necam\OneDrive\1 Projects\ROS2-DifferentialRobot_Repository_Project\Assets (For README)\recordingdiffrobot_pkg.mp4
(https://github.com/Nectar-A-Gonzalez/ROS2-DifferentialRobot_Repository_Project/Assets/recordingdiffrobot_pkg.mp4)
=======

>>>>>>> cb4e8465d31402872d1b092f3b150b353e2822e4
