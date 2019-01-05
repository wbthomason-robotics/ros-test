#!/usr/bin/env python2
import rospy
import numpy as np
from turtlesim.srv import Spawn
from random import randint, choice
from p1.srv import *
from geometry_msgs.msg import Twist


def draw_flower():

    # initialize 'drawing_turtle' node
    # FILL IN
    # use custom draw service
    # blocks while waiting for service to become available
    #rospy.wait_for_service(FILL IN)
    try:
        # create a handle for calling the draw service
        #draw = rospy.ServiceProxy(FILL IN , FILL IN )
        pass
    except rospy.ServiceException as ex:
        rospy.logerr('Could not draw turtle! Exception: {}'.format(ex))
        rospy.signal_shutdown("Couldn't draw!")

    # create velocity publisher and set the publishing rate of 5
    #velocity_publisher = FILL IN
    #rate = FILL IN

    times = 1
    max_times = 7
    count = 0
    rotate = 0
    while not rospy.is_shutdown():
        # use the draw service to get the velocity message to publish
        # see srv.Draw.srv for specifics on the parameters and return value of the draw service 
        # vel_msg = FILL IN
        # publish the message
        # FILL IN
        # FILL IN
        rotate = 0
        count += 0.1
        if count > 2 * times * np.pi:
            times += 1
            rotate = 1
            if times > max_times:
                rospy.spin()

if __name__ == '__main__':
    # call appropriate function
    # FILL IN
    pass
