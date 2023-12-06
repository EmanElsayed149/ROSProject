#!/usr/bin/env python3
import rospy

from my_robot_controller.msg import MyTwist   #my_robot_controller is >>> package name 
                                              #MyTwist is >>> filename.msg

if __name__ == '__main__':
   rospy.init_node("publisher2_node")
   rospy.loginfo("publishing starting .....")

   pub = rospy.Publisher("turtle1/cmd_vel",MyTwist,queue_size =10)     #turtle1/cmd_vel topic name (can be any thing but I choose this for turtlesim node)
   rate = rospy.Rate(1)
   i = 0 
   while not rospy.is_shutdown() :
      twist = MyTwist()
      twist.linear.x = 1.0
      twist.angular.z= 0.9
      pub.publish(twist)
      rospy.loginfo('publishing: ....')
      rate.sleep()
