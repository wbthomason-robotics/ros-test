#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import Float32
import numpy as np
"""Learn how to move a turtle using Twist messages.
    Calculate distance between turtle and a point."""


class Turtle:

  def __init__(self):
    pass

  def move(self):

    start_time = rospy.Time.now().to_sec()
    # move for about 1 second
    while not rospy.is_shutdown() and rospy.Time.now().to_sec() - start_time < 1:
      pass

    def update_pose(self, data):
      pass

    def calculate_distance(self, x, y):
      """Calculate the Euclidean distance, using vector operations, from the turtle's current
      position to the point (x,y). Set the result as a ros param, named distance."""

    # set ros parameter to be the distance
    pass


if __name__ == '__main__':
  try:
    turtle = Turtle()
    turtle.move()
    turtle.calculate_distance(1, 1)
  except rospy.ROSInterruptException:
    pass
