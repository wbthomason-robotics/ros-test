#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import numpy as np


""" Use numpy to draw a flower."""
class FlowerTurtle:

    def __init__(self):
        # Start a new node named 'flower'
        # FILL IN
        # Define a publisher for '/turtle1/cmd_vel' topic with a queue size of 10
        # FILL IN
        # Set the rate to be 5
        # FILL IN
        pass

    def draw_flower(self):

        # calculate constant values, see written assignment
        # a = FILL IN
        # b = FILL IN
        # A = FILL IN
        # B = FILL IN
        # max_times = FILL IN

        # set the values of the above constants to rosparams (see problem 1 for reference)
        # the rosparams should be named: 'a', 'b', 'A', 'B', 'max_times' and should be of type float

	# FILL IN

        count = 0
        times = 1
        while not rospy.is_shutdown():

            """ Publish velocity message with angular z = B * cos(b*count)
                and linear x = A * sin(a*count). Use numpy for trig operations."""
            # FILL IN

            count += 0.1

            """ If count is greater than 2(times)(PI), publish a
                velocity message with angular z = 5.
                Then increment times by 1.
                If times is greater than max_times stop drawing the flower.
               """

	     # FILL IN


if __name__ == '__main__':
    try:
        # Call the appropriate functions so that the turtle draws a flower.
        pass
    except rospy.ROSInterruptException: pass
