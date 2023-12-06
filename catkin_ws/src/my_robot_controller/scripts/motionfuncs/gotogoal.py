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
   
def go_to_goal(velocity_publisher , x_goal , y_goal ):
   
   global x,y,theta
   
   #const for rp_contrller 
   k_linear = 0.2 
   k_angular = 4.0
   
   #object of Twist 
   velocity_message = Twist()
   rate = rospy.Rate(10)
   
   while (True):
      #distance between current position and goal 
      distance = abs( math.sqrt( ((x-x_goal)**2) + ((y-y_goal)**2)  ))
      linear_speed = distance * k_linear 
      
      #angle to rotate 
      angle = math.atan2( y_goal-y , x_goal-x ) 
      angular_speed = k_angular * (angle - theta)
      
      if(distance < .01):
         velocity_message.linear.x = 0.0
         velocity_message.angular.z = 0.0
         velocity_publisher.publish(velocity_message)
         print('finally reached ')
         break
      else :
         velocity_message.linear.x = linear_speed
         velocity_message.angular.z = angular_speed
     
      velocity_publisher.publish(velocity_message)
      print('x= ', x , ',y= ' , y , ',distance= ' , distance)
      rate.sleep()
      
if __name__ == "__main__":
   rospy.init_node('turtlesim_go_to_goal')
   
   velocity_topic = '/turtle1/cmd_vel'
   velocity_publisher = rospy.Publisher(velocity_topic , Twist , queue_size = 10)
   
   position_topic = '/turtle1/pose'
   position_subscriber = rospy.Subscriber(position_topic , Pose , posecallback)
   
   #sleeep until first subscribing
   time.sleep(2)
   
   go_to_goal(velocity_publisher , 2.0, 10.0)
