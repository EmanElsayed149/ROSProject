#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction , MoveBaseGoal
from math import radians , degrees 
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point

def move_to_goal(xgoal , ygoal ):
   # define clinet to sent goal request to the move_base server 
   ac = actionlib.SimpleActionClient("move_base" , MoveBaseAction)  
   
   #wait for the action server to come up
   while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
      rospy.loginfo("waiting for the move_base action server to come up")
   goal = MoveBaseGoal()
   
   #set up the frame parameter 
   goal.target_pose.header.frame_id = "map"
   goal.target_pose.header.stamp = rospy.Time.now()
   
   #moving towards the goal
   goal.target_pose.pose.position.x = xgoal 
   goal.target_pose.pose.position.y = ygoal 
   goal.target_pose.pose.position.z = 0
   
   goal.target_pose.pose.orientation.x = 0.0
   goal.target_pose.pose.orientation.y = 0.0
   goal.target_pose.pose.orientation.z = 0.0
   goal.target_pose.pose.orientation.w = 1.0
   
   rospy.loginfo("sending goal location ....")
   ac.send_goal(goal)
   
   ac.wait_for_result(rospy.Duration(60))
   
   if(ac.get_state() == GoalStatus.SUCCEEDED):
      rospy.loginfo("you have reached the destination")
   else:
      rospy.loginfo("therobot failed to reach the destination")
      
if __name__ == '__main__':
    rospy.init_node('map_navigation',anonymous=False)
    x_goal = -2.02880191803
    y_goal = 4.02200937271
    
    print('start go to goal ')
    move_to_goal (x_goal , y_goal )
    rospy.spin()
