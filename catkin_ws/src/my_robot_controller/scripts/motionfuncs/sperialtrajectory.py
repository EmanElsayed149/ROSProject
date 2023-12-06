#!/usr/bin/env python3

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time 
import rospy


def posecallback(position_message):
   global x,y, theta
   x = position_message.x
   y = position_message.y
   
   
def sperialtrajectory(velocity_publisher ,k_linear , k_angular):
   global x , y
   rate = rospy.Rate(1)
   velocity_message = Twist()
   while(True):
      k_linear = k_linear + 0.4
      if((x<10) and (y<10)):
         velocity_message.linear.x = k_linear 
         velocity_message.angular.z = k_angular 
         velocity_publisher.publish(velocity_message)
         rate.sleep()
      else:
         print('oh no! I get tired ')
         break
if __name__ == "__main__":
   rospy.init_node('turtlesim_sperial_trajectory')
   
   velocity_topic = '/turtle1/cmd_vel'
   velocity_publisher = rospy.Publisher(velocity_topic , Twist , queue_size = 10)
   
   position_topic = '/turtle1/pose'
   position_subscriber = rospy.Subscriber(position_topic , Pose , posecallback)
   
   #sleeep until first subscribing
   time.sleep(2)
   
   sperialtrajectory(velocity_publisher , 0.0 , 5.0)


