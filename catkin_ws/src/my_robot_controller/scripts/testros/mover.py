#!/usr/bin/env python3
import rospy

from geometry_msgs.msg import Twist



if __name__ == '__main__':
   rospy.init_node("mover_node")
   rospy.loginfo("starting .....")
   cmdvel = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size =10)
   rate = rospy.Rate(1)
  
   while not rospy.is_shutdown() :
      twist = Twist()
      twist.linear.x=1.5
      twist.angular.z=1.0 
      cmdvel.publish(twist)
      rate.sleep()
