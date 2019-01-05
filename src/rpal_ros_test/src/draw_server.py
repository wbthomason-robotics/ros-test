#!/usr/bin/env python

from geometry_msgs.msg import Twist
import rospy
import numpy as np

from rpal_ros_test.srv import Draw


# draw service, see Draw.srv for parameters and return values
def draw(req):
  pass


def draw_server():
  '''The server for the draw service'''
  rospy.init_node('draw_server')
  rospy.loginfo('Started up!')
  # make service here
  rospy.spin()
  rospy.loginfo('Shutting down!')


if __name__ == '__main__':
  # start draw server
  pass
