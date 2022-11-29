# Move2Point
A module used for controlling robot arm via script after setting up a moveit package of your robot

## Setup
1. Download this package and place it in the src folder of your workspace
2. Build your workspace and resource the bashrc
```
catkin_make
source ~/.bashrc
```
3. Import the module by adding the following line to your script
```python
from move2point import send_goal
```