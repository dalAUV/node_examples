#!/usr/bin/env python 
import rospy
from std_msgs.msg import String 
# Callback when new data is published to node
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
# Listener Function 
def listener():
    rospy.init_node('listener_py', anonymous=True)
    # Set node to sub to, set callback when data is received 
    rospy.Subscriber("chatter_py", String, callback)
    # stops script from ending
    rospy.spin()
# Start of Script
if __name__ == '__main__':
    listener()