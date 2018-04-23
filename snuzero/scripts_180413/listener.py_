#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String
from snuzero.msg import ser_com

def callback(data):
    print("###Listener Node###")
    if data.am == 1:
        print("Automatic Mode")
    else:
        print("Menual Mode")
    print("SPEED : " + str(data.speed))
    print("STEER : " + str(data.steer))
    print("ALIVE : " + str(data.alive))
def listener():
    rospy.init_node('serial_listener', anonymous=True)
    rospy.Subscriber("serial_topic", ser_com, callback)
    print("#" * 30)
    print("Serial Communication Listener Node Running!")
    print("#" * 30)
    
    rospy.spin()
    
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
