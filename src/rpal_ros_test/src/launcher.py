#!/usr/bin/env python2
'''Launch a random number of drawing turtles'''

from random import randint

import roslaunch
import rospy

"""launch the draw_turtle.py node x times"""

def run():

  rospy.init_node('draw_launcher')
  draw = roslaunch.Node('p1', 'problem4b.py')
  num_turtles = randint(2, 5)
  rospy.loginfo('Starting launcher')
  launch = roslaunch.scriptapi.ROSLaunch()
  launch.start()
  procs = []
  rospy.loginfo('Launching {} turtles'.format(num_turtles))
  for i in range(num_turtles):
    # The spawn service is sometimes dumb, so we add a delay between calls
    draw.name = 'draw_turtle{}'.format(i)
    procs.append(launch.launch(draw))
    rospy.loginfo(draw.name)
    rospy.sleep(1)

  rospy.loginfo('Spinning!')
  rospy.spin()


if __name__ == '__main__':
  run()
