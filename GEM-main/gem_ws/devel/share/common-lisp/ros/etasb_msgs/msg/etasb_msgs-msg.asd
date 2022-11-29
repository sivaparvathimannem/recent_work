
(cl:in-package :asdf)

(defsystem "etasb_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "point2D" :depends-on ("_package_point2D"))
    (:file "_package_point2D" :depends-on ("_package"))
    (:file "point2DArray" :depends-on ("_package_point2DArray"))
    (:file "_package_point2DArray" :depends-on ("_package"))
  ))