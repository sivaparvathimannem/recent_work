# Folder Description
## gem_bringup
complete launches
## gem_gazebo
everything that describes the gazebo world including props
## model_description
objects with joint
> ## yaskawa_hc10
> Yaskawa robot arm
> ## test_stand
> the platform where yaskawa robot, cameras are placed
> ## gripper
> the gripper that is attached to the yaskawa robot
## gem_moveit
trajectory planning with moveit. 
## move2point
it contains script that can send goal (position/joint_state) for the robot
## hc10
working package that can control the robot via moveit, provide by Patrik Cönen
# Launches
1. Launching the simulation
```
roslaunch gem_bringup standard.launch
```
2. Launching the simulation together with moveit
```
roslanch gem_moveit demo_gazebo.launch
```
> execute predefined joint positions
```
rosrun gem_moveit pick_n_place.py
```
3. Control the physical robot via moveit
```
rosrun hc10_control bringup.launch robot_ip:=192.168.1.74
```

# Tools
list all the devices connected to your network
```
nmap -sP 192.168.1.0/24
```