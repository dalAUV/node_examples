#!/usr/bin/env python 
from unittest import expectedFailure
import rospy
from std_msgs.msg import String 

# Publisher Function 
def talker():
    # Create Node
    pub = rospy.Publisher('chatter_py', String, queue_size=10)
    rospy.init_node('talker_py' ,anonymous=True)
    # Set loop rate, loop 10 times per second 
    rate = rospy.Rate(10) #10 Hz
    # loop until roscore is shutdown/exited or crtl+c is caught
    while not rospy.is_shutdown():
        # Generated and Publish Message
        hello_str = "Hello World %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        # sleep for set rate
        rate.sleep()
# Start of Script 
if __name__ == '__main__':
    try:
        talker()
    # to Catch sleep() and exit signals    
    except rospy.ROSInterruptException:
        pass
    