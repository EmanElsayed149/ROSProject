
(cl:in-package :asdf)

(defsystem "my_robot_controller-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "MyTwist" :depends-on ("_package_MyTwist"))
    (:file "_package_MyTwist" :depends-on ("_package"))
  ))