#!/usr/bin/env python2
import rospy
import numpy as np
from turtlesim.srv import Spawn
from random import randint, choice
from rpal_ros_test.srv import Draw
from geometry_msgs.msg import Twist


def draw_flower():
  # Put your initialization code here

  times = 1
  max_times = 7
  count = 0
  rotate = 0

  # Main loop
  while not rospy.is_shutdown():
    # Create velocity message here
    rotate = 0
    count += 0.1
    if count > 2 * times * np.pi:
      times += 1
      rotate = 1
      if times > max_times:
        rospy.spin()


if __name__ == '__main__':
  # Call appropriate function
  pass
