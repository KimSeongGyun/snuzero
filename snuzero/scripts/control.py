#!/usr/bin/env python
# license removed for brevity
# input : steer-degree, speed:m/s

import rospy
import time
import serial
import math
from std_msgs.msg import String
from snuzero.msg import control

def init():

    pub = rospy.Publisher('control_topic', control, queue_size=10)
    rospy.init_node('control_sender', anonymous=True)
    rate = rospy.Rate(20)
    msg = control()
   
    while not rospy.is_shutdown():
            
      
        rospy.loginfo(msg)

        am=1
        estop=0
        gear=0
        speed=0 #m/s
        steer=11.5 #degree
        brake=1
        
        msg.am = am
        msg.estop = estop
        msg.gear = gear
        msg.brake = brake
        msg.speed = round(speed,3)
        msg.steer = round(steer,3)
        msg.encoder = 100
        
        pub.publish(msg)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        init()
    except rospy.ROSInterruptException:
        pass
