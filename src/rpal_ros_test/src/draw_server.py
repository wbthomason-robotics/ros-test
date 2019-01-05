#!/usr/bin/env python

from geometry_msgs.msg import Twist
import rospy
import numpy as np

from p1.srv import Draw



# draw service, see draw.srv for parameters and return values
def draw(req):


    # initalize vel_msg
    # FILL IN

    # set count to be the count parameter
    # count = FILL IN

    # calculate constant values, see written assignment
    # a = FILL IN
    # b = FILL IN
    # A = FILL IN
    # B = FILL IN


    # set the values of the above constants to rosparams (see problem 1 for reference)
    # the rosparams should be named: 'a', 'b', 'A', 'B' and should be of type float
    # FILL IN

    # if rotate is true set the angular velocity to -3
    if req.rotate:
        # FILL IN
       pass
    # otherwise set angular z = B * cos(b*count)
    # and linear x = A * sin(a*count). Use numpy for trig operations.
    else:
        # FILL IN
        pass

    # return return value
    #return FILL IN

def draw_server():
  '''The server for the draw service'''
  rospy.init_node('draw_server')
  rospy.loginfo('Started up!')
  # Create service with name: 'draw',  service_class: Draw, and handler: draw
  #rospy.Service(FILL IN, FILL IN, FILL IN)
  rospy.spin()
  rospy.loginfo('Shutting down!')


if __name__ == '__main__':
    # start draw server
    # FILL IN
    pass
