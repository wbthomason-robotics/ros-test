#!/usr/bin/env python
'''Provide youBot arm configurations as angles for p3'''

from math import radians
from random import uniform

import rospy
import numpy as np
from p3.srv import Problem1 as KinService
from p3.msg import JointAngles, PointArray
from std_msgs.msg import Float64
from geometry_msgs.msg import Point

class ArmConfig:

	def __init__(self):
		# subscriber to help keep track of joint angles
		rospy.Subscriber("/vrep/youbot/arm/pose", JointAngles, self.joint_angle_callback)

		self.angles = [0,0,0,0,0]

		# publishers for valid config (on visible youBot)
		self.arm_pubs = [
			rospy.Publisher('vrep/youbot/arm/joint{}/angle'.format(i), Float64, queue_size=10)
			for i in range(1,6)
		]

                rospy.wait_for_service('fk')
                self.fk = rospy.ServiceProxy('fk', KinService)

                self.target_pub = rospy.Publisher('/vrep/youbot/target/position', PointArray, queue_size=10)

                self.debug = rospy.get_param('~fk_debug', False)
                print "Debug mode is: %s" % self.debug

                # for debug mode
                self.theta_rates = [0.01, 0.01, 0.01, 0.01, 0.01]
                self.thetas = [0, 0, 0, 0, 0]

                # joint limits are symmetric about zero
                self.limits = [radians(169), radians(90), radians(131),
			       radians(102), radians(90)]


	def pub_config(self):
		# generate random config and publish to p3/arm_config
                if self.debug:
                    config = self.gen_config_debug()
                else:
                    config = self.gen_config()

                # compute fk from student's service
                joint_angles = JointAngles()
                joint_angles.angles = config
                pts = self.fk(joint_angles)

                # for debug mode, shift the balls foward so they don't overlap the arm
                if self.debug:
                    for pt in pts.points.points:
                        pt.x += 0.4

                # command ball position
                self.target_pub.publish(pts.points)

		# also publish to actual youBot arm
		for pub, val in zip(self.arm_pubs, config):
			pub.publish(val)


	def gen_config_debug(self):
            for ii in range(5):
                self.thetas[ii] += self.theta_rates[ii]
                if self.thetas[ii] * np.sign(self.theta_rates[ii]) >= self.limits[ii]:
                    self.theta_rates[ii] = -self.theta_rates[ii]
            return self.thetas


	def gen_config(self):
		# create and return a valid arm config
                return [ uniform(-ll, ll) for ll in self.limits ]

	def joint_angle_callback(self, data):
		self.angles = data.angles


if __name__ == '__main__':
	rospy.init_node('arm_config', anonymous=True)

	arms = ArmConfig()
        if arms.debug:
            rate = rospy.Rate(5)
        else:
            rate = rospy.Rate(1)

	while not rospy.is_shutdown():
		arms.pub_config()
		rate.sleep()
