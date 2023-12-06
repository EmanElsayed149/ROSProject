#!/usr/bin/env python3

from my_robot_controller.srv import AddTwoInts
from my_robot_controller.srv import AddTwoIntsRequest
from my_robot_controller.srv import AddTwoIntsResponse

import rospy
import sys

def add_two_ints_client(x,y):
   #wait until server become ready
   rospy.wait_for_service('add_two_ints')
   try:
      c = rospy.ServiceProxy('add_two_ints',AddTwoInts)
      resp = c(x,y)
      return resp.result
   except rospy.ServiceException(e):
      print("Service call failed : %s" % e)
if __name__ == "__main__":
   if len(sys.argv) == 3:
      x = int(sys.argv[1])
      y = int(sys.argv[2])
   else:
      print("%s [x y] " % sys.argv[0])
      sys.exit(1)
   print("Responding %s+%s" % (x,y))
   s = add_two_ints_client(x, y)
   print("%s + %s = %s" % (x,y,s))
