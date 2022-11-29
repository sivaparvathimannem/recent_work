1. Connect to the physical robot. Remember to change it to your robot's ip
```
roslaunch hc10_control bringup.launch robot_ip:=192.168.1.74
```
2. Change the mode on the pendant to remote control by turning the key fully clockwise.

3. Enable the servo motor
```
rosservice call /robot_enable
```