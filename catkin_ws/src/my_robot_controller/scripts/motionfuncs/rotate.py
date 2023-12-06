#!/usr/bin/env python3

import rospy
import time
import math 

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def posecallback(position_message):
   global theta 
   theta = position_message.theta
      
def rotate(velocity_publisher , angular_speed_deg , relative_angle_degree, is_clockwise):
   global theta
   #object of twist for publishing angular speed
   cmd_vel_message = Twist()
   theta0 = math.degrees(theta)
   #convert angular speed to radian degree 
   angular_speed_rad = math.radians( abs(angular_speed_deg) ) 
   
   if (is_clockwise):
      cmd_vel_message.angular.z = -abs(angular_speed_rad)
      desired_angle = (theta0-relative_angle_degree)
   else:
      cmd_vel_message.angular.z = abs(angular_speed_red)
      desired_angle = (theta0+relative_angle_degree)
   print(desired_angle)
   while(True):
     
      current_angle = math.degrees(theta)
      print(current_angle)
      
      if(abs(current_angle-desired_angle) <=1):
         rospy.loginfo('reached')
         break
      else :
         velocity_publisher.publish(cmd_vel_message)
   cmd_vel_message.angular.z=0
   velocity_publisher.publish(cmd_vel_message)
   
if __name__ == "__main__":
   
   rospy.init_node('turtlesim_rotation_motion')
   
   cmd_vel_topic = '/turtle1/cmd_vel'
   velocity_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)
  
   position_subsriber = rospy.Subscriber('/turtle1/pose',Pose, posecallback)
   time.sleep(4)
   rotate(velocity_publisher , 10.0, 90, True)
   
