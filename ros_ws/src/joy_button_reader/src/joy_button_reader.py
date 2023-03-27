#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy

def callback(data):
	buttons_abxy = data.buttons[:4]
	if any(buttons_abxy):
		print(buttons_abxy)

    # Intializes everything
def start():
        # subscribed to joystick inputs on topic "joy"
        rospy.Subscriber("joy", Joy, callback)
        # starts the node
        rospy.init_node("joy_button_reader", anonymous=True)
        rospy.spin()

if __name__ == '__main__':
	start()
