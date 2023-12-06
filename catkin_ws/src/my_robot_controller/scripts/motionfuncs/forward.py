#!/usr/bin/env python3

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import rospy
import math
import time

def posecallback(pose_message):
   global x
   global y
   x = pose_message.x
   y = pose_message.y
   
def move(velocity_publisher,speed,distance,is_forward):
   velocity_message = Twist()
   #get current location
   global x
   global y
   x0 = x
   y0 = y
   if (is_forward):
      velocity_message.linear.x = abs(speed)
   else:
      velocity_message.linear.x = -abs(speed)
   distance_moved = 0.0
   rate = rospy.Rate(10)
   
   while True:
      rospy.loginfo('turtlesim moves forward')
      velocity_publisher.publish(velocity_message)
      rate.sleep()
      
      distance_moved = abs(math.sqrt( ((x-x0)** 2) + ((y-y0)**2)  ) )
      print(distance_moved)
      
      if(not (distance_moved<distance)):
         rospy.loginfo('turtlesim reached')
         break
   velocity_message.linear.x=0
   velocity_publisher.publish(velocity_message)
      
      
      
   
if __name__ == '__main__':
   try:
      rospy.init_node("turtlesim_forwardmotion")
      
      cmd_vel_topic = "/turtle1/cmd_vel"
      velocity_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)
      
      position_topic = "/turtle1/pose"
      pose_subsriber = rospy.Subscriber(position_topic,Pose,posecallback)
      #delay call o move until subscribing x , y position 
      time.sleep(5)
      
      move(velocity_publisher, 1.0 , 4.0 ,True)
      
   except rospy.ROSInterruptException:
      rospy.loginfo('node terminated.')
      
      
