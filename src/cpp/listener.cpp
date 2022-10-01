#include "ros/ros.h"
#include "std_msgs/String.h"

void chatterCallback(const std_msgs::String::ConstPtr& msg){
    ROS_INFO("Heard: >> %s <<", msg->data.c_str());
}
int main(int argc, char **argv){
    ros::init(argc, argv, "listener_CPP");

    ros::NodeHandle node;

    ros::Subscriber sub = node.subscribe("Hello_CPP", 1000, chatterCallback);

    ros::spin();

    return 0;
}