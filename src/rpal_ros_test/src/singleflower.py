#!/usr/bin/env python2
import rospy
from geometry_msgs.msg import Twist
import numpy as np


class FlowerTurtle:
  """ Use numpy to draw a flower."""

  def __init__(self):
    pass

  def draw_flower(self):
    count = 0
    times = 1
    while not rospy.is_shutdown():
      # Use numpy for trig operations.

      count += 0.1


if __name__ == '__main__':
  try:
    # Call the appropriate functions so that the turtle draws a flower.
    pass
  except rospy.ROSInterruptException:
    pass
