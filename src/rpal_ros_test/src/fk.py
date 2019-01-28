#!/usr/bin/env python2

import rospy
from rpal_ros_test.msg import JointAngles, PointArray
from rpal_ros_test.srv import Fk as KinService
from functools import partial
from geometry_msgs.msg import Point
from std_msgs.msg import Float64
import numpy as np
import math


class YouBotFK:
  '''This is a standalone foward kinematics service for the KUKA YouBot'''

  def __init__(self):
    # Initialize a service called 'fk'
    pass

  def dh_matrix(self, theta, d, a, alpha):
    '''Return a Denavit-Hartenberg matrix with the provided parameters'''
    pass

  def callback(self, req):
    '''Handle FK queries by returning a PointArray containing each frame
    origin in the arm.  The final element of the PointArray is the
    end-effector position.'''
    pass


if __name__ == "__main__":
  rospy.init_node('fk')
  fk = YouBotFK()
  rospy.spin()
