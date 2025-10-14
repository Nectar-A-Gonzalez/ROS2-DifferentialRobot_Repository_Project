# DiffRobot_pkg
These packages are used to model a differential drive robot that communicates via ROS2 - Jazzy Distro.
The diffrobot_pkg includes the three nodes that are used to simulate the differential robots behavior.
The behavior is as follows:<br>
- The robot is given a velocity at which it should move, the encoders are to dfdfd
- The encoders read the angular velocity of each wheel in terms of tics read per degree dfdf
 
- #Communicates to what Explain the ros way of communicating or just the data processing aspect, I think only the logical part #IDEA
- #And maybe give instrutions to how to see ros communication nodes relationships. #IDEA

> [!Note] 
> The instructions given here are for a Linux OS dfdfdfdfdfd
jkjjkj


## How to build the package in your own workspace:
To build the package in a workspace, you first need to create your workspace folder (if you don't already have one).<br>


### To create a workspace
To do that, in a terminal window write:

    mkdir -p ros2_ws/src dfdfdfdff
    dfdf
    sdsdsd

After creating your workspace, add the necessary workspace folders

    dfdfd
    dfdfdf
    dfdf

Finally, add the DiffRobot packages (diffrobot_pkg and diffrobot_interfaces).

    dfdf

Here the diffrobot_pkg hold the dfdfdffdf code, while diffrobot_interfaces holds the necessary msg and srv templates for ROS2 communication.


## Commands to test the pub/sub and service/client communications:
sdsdsdsd<br>

To simulate a commanding velocity input, dfdf<br>

    ros2 pub dfdfdf at -rate 10
    dfd
    klklkl

dfdfdf<br>

    df
    dfdf

## Example Outputs Video - Using the test commands



### Some References<br>
[Differential Drive Kinematics Notes by The University of Columbia](https://www.cs.columbia.edu/~allen/F17/NOTES/icckinematics.pdf "CS W4733 NOTES - Differential Drive Robots")<br>
[Kinematics of Differential Drive Robots and Odometry
Video by Engineering Educator Academy](https://www.youtube.com/watch?v=RZlZcDxQ8P4 "Kinematics of Differential Drive Robots and Odometry")
