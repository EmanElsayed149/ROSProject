#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


if __name__ == '__main__':
   rospy.init_node("publisher_node")
   rospy.loginfo("publishing starting .....")

   pub = rospy.Publisher("mytopic",String,queue_size =10)
   rate = rospy.Rate(1)
   i = 0 
   while not rospy.is_shutdown() :
      msg= String()
      msg.data = "Hello:%d"% i 
      pub.publish(msg)
      rospy.loginfo('publishing "%s" ' % msg.data)
      i+=1
      rate.sleep()
