#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import Float32
import numpy as np

"""Learn how to move a turtle using Twist messages.
    Calculate distance between turtle and a point."""


class Turtle:

    def __init__(self):
        # Starts a new node
        rospy.init_node('move', anonymous=True)

        # Subscribe to /turtle1/pose with callback, self.update_pose
        #self.pose_subscriber = rospy.Subscriber(FILL IN)
        self.pose = Pose()

        # Create a publisher that publishes to /turtle1/cmd_vel
        #self.velocity_publisher = rospy.Publisher(FILL IN, queue_size=10)


        # Specify publishing rate of 10
        #self.rate = FILL IN

    # move the turtle
    def move(self):

        # Create a Twist message with values that change the turtle's
        # linear and angular velocities
        #vel_msg = FILL IN

        start_time = rospy.Time.now().to_sec()
        # move for about 1 second
        while not rospy.is_shutdown() and rospy.Time.now().to_sec() - start_time < 1:

            # publish the Twist message to the velocity publisher
            # FILL IN

            #specify publishing rate (uncomment after rate is set above)
            #self.rate.sleep()
            pass
    # set the global pose variable to the data received from the subscriber
    def update_pose(self, data):
        # FIll IN
        pass

    """Calculate the Euclidean distance, using vector operations,
       from the turtle's current position to the point (x,y).
        Set the result as a ros param, named distance."""
    def calculate_distance(self, x, y):

        # use vectors, do not add any more lines here
        #vector = FILL IN
        #distance = FILL IN

        # set ros parameter to be the distance
	    # Note: you will need to cast the distance value to a float
        #rospy.set_param('distance', FILL IN)
        pass


if __name__ == '__main__':

    try:
        turtle = Turtle()
        turtle.move()
        turtle.calculate_distance(1, 1)
    except rospy.ROSInterruptException:
        pass
