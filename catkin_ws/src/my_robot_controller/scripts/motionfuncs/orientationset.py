#!/usr/bin/env python3

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import rospy
import math
import time

def posecallback(position_message):
   global x,y, theta
   x = position_message.x
   y = position_message.y
   theta = position_message.theta
def set_desired_orientation(velocity_publisher , desired_angle_degree):
   #object of cmd_vel
   velocity_message = Twist()
   
   #const for p_controller
   k_angular = 4.0
   
   #rate 
   rate = rospy.Rate(10)
   #start rotate 
   while(True):
      relative_angle = math.radians(desired_angle_degree) - theta
      angular_speed = k_angular*relative_angle 
      velocity_message.angular.z = angular_speed
      
      if(abs(relative_angle) < .0001):
         velocity_message.angular.z = 0.0  
         velocity_publisher.publish(velocity_message)
         print('set orientation is done ')
         break 
      velocity_publisher.publish(velocity_message) 
      print('current orientation = ',math.degrees(theta))
      rate.sleep()
   
   
   
   
   
if __name__ == "__main__":
   rospy.init_node('turtlesim_go_to_goal')
   
   velocity_topic = '/turtle1/cmd_vel'
   velocity_publisher = rospy.Publisher(velocity_topic , Twist , queue_size = 10)
   
   position_topic = '/turtle1/pose'
   position_subscriber = rospy.Subscriber(position_topic , Pose , posecallback)
   
   #sleeep until first subscribing
   time.sleep(2)
   
   set_desired_orientation(velocity_publisher , -170.0)
