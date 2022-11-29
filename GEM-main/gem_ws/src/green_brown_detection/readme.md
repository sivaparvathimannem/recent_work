# Description
Apply green brown detection on an image feed and gives out the center point of the green objects

# Subscribed topic
- daheng_camera/image_raw ([sensor_msg/Image](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/Image.html))
>>> image feed topic

# Publish topic
- image_with_contour ([sensor_msg/Image](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/Image.html))
>>> image feed with contour on green objects
- chain ([etasb_msgs.msg import point2DArray]())
>>> an array with the center point of the green objects
