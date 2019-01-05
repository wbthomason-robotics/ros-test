#!/usr/bin/env python2
import rospy
import numpy as np
from turtlesim.srv import Spawn
from random import randint, choice
from rpal_ros_test.srv import Draw
from geometry_msgs.msg import Twist


def draw_flower():
  try:
    # create a handle for calling the spawn service
    pass
  except rospy.ServiceException as ex:
    rospy.logerr('Could not spawn turtle! Exception: {}'.format(ex))
    rospy.signal_shutdown("Couldn't spawn!")

  try:
    # set turtle name
    # Spawn turtle at random coordinates (hint: [3, 8] is a reasonable range for x and for y)
    pass
  except rospy.ServiceException as ex:
    rospy.logerr('Could not spawn turtle! Exception: {}'.format(ex))
    rospy.signal_shutdown("Couldn't spawn!")

  # use custom draw service

  times = 1
  max_times = 4
  count = 0
  rotate = 0
  while not rospy.is_shutdown():
    # use the draw service to get the velocity message to publish
    # publish message

    rotate = 0
    count += 0.1
    if count > 2 * times * np.pi:
      times += 1
      rotate = 1
      if times > max_times:
        rospy.spin()


if __name__ == '__main__':
  # call the appropriate function
  pass
