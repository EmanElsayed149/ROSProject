#!/usr/bin/env python3

from my_robot_controller.srv import AddTwoInts
from my_robot_controller.srv import AddTwoIntsRequest
from my_robot_controller.srv import AddTwoIntsResponse

import rospy


def handel_add_two_ints(req):
   print('successfully added')
   return AddTwoIntsResponse(req.num1+req.num2)

def addtwointsserver():
   rospy.init_node('add_two_ints_server')
   s = rospy.Service('add_two_ints',AddTwoInts,handel_add_two_ints)
   print("ready to add two ints")
   rospy.spin()
   
if __name__ == "__main__":
   addtwointsserver()
