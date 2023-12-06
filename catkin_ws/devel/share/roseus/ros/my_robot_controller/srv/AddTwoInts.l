;; Auto-generated. Do not edit!


(when (boundp 'my_robot_controller::AddTwoInts)
  (if (not (find-package "MY_ROBOT_CONTROLLER"))
    (make-package "MY_ROBOT_CONTROLLER"))
  (shadow 'AddTwoInts (find-package "MY_ROBOT_CONTROLLER")))
(unless (find-package "MY_ROBOT_CONTROLLER::ADDTWOINTS")
  (make-package "MY_ROBOT_CONTROLLER::ADDTWOINTS"))
(unless (find-package "MY_ROBOT_CONTROLLER::ADDTWOINTSREQUEST")
  (make-package "MY_ROBOT_CONTROLLER::ADDTWOINTSREQUEST"))
(unless (find-package "MY_ROBOT_CONTROLLER::ADDTWOINTSRESPONSE")
  (make-package "MY_ROBOT_CONTROLLER::ADDTWOINTSRESPONSE"))

(in-package "ROS")





(defclass my_robot_controller::AddTwoIntsRequest
  :super ros::object
  :slots (_num1 _num2 ))

(defmethod my_robot_controller::AddTwoIntsRequest
  (:init
   (&key
    ((:num1 __num1) 0)
    ((:num2 __num2) 0)
    )
   (send-super :init)
   (setq _num1 (round __num1))
   (setq _num2 (round __num2))
   self)
  (:num1
   (&optional __num1)
   (if __num1 (setq _num1 __num1)) _num1)
  (:num2
   (&optional __num2)
   (if __num2 (setq _num2 __num2)) _num2)
  (:serialization-length
   ()
   (+
    ;; int32 _num1
    4
    ;; int32 _num2
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _num1
       (write-long _num1 s)
     ;; int32 _num2
       (write-long _num2 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _num1
     (setq _num1 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _num2
     (setq _num2 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass my_robot_controller::AddTwoIntsResponse
  :super ros::object
  :slots (_result ))

(defmethod my_robot_controller::AddTwoIntsResponse
  (:init
   (&key
    ((:result __result) 0)
    )
   (send-super :init)
   (setq _result (round __result))
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; int32 _result
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _result
       (write-long _result s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _result
     (setq _result (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass my_robot_controller::AddTwoInts
  :super ros::object
  :slots ())

(setf (get my_robot_controller::AddTwoInts :md5sum-) "4bac5263dd214a8605f1874d4917e35b")
(setf (get my_robot_controller::AddTwoInts :datatype-) "my_robot_controller/AddTwoInts")
(setf (get my_robot_controller::AddTwoInts :request) my_robot_controller::AddTwoIntsRequest)
(setf (get my_robot_controller::AddTwoInts :response) my_robot_controller::AddTwoIntsResponse)

(defmethod my_robot_controller::AddTwoIntsRequest
  (:response () (instance my_robot_controller::AddTwoIntsResponse :init)))

(setf (get my_robot_controller::AddTwoIntsRequest :md5sum-) "4bac5263dd214a8605f1874d4917e35b")
(setf (get my_robot_controller::AddTwoIntsRequest :datatype-) "my_robot_controller/AddTwoIntsRequest")
(setf (get my_robot_controller::AddTwoIntsRequest :definition-)
      "int32 num1
int32 num2
---
int32 result

")

(setf (get my_robot_controller::AddTwoIntsResponse :md5sum-) "4bac5263dd214a8605f1874d4917e35b")
(setf (get my_robot_controller::AddTwoIntsResponse :datatype-) "my_robot_controller/AddTwoIntsResponse")
(setf (get my_robot_controller::AddTwoIntsResponse :definition-)
      "int32 num1
int32 num2
---
int32 result

")



(provide :my_robot_controller/AddTwoInts "4bac5263dd214a8605f1874d4917e35b")


