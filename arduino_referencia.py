#!/usr/bin/env python

import rospy
import serial
import math
import time
from geometry_msgs.msg import Twist
ser = serial.Serial('/dev/ttyACM0',115200)


def callback(msg):
        V=msg.linear.x 
        W=msg.angular.z
#Message
        if V<0:
                Vmsb=int(128+abs(V)//256)
                Vlsb=int(abs(V)%128)

        else:
                Vmsb=int(abs(V)//256)
                Vlsb=int(abs(V)%128)
        if W<0:
                Wmsb=int(128+abs(W)//256)
                Wlsb=int(abs(W)%128)
        else:
                Wmsb=int(abs(W)//256)
                Wlsb=int(abs(W)%128)

        if (200+1+Vlsb+Vmsb+Wlsb+Wmsb)%256==0:
                cheacksum=int(0)
        else:
                cheacksum=int(256-(200+1+Vlsb+Vmsb+Wlsb+Wmsb)%256)
        ser.write(bytearray([int(200),int(1),Vlsb,Vmsb,Wlsb,Wmsb,cheacksum]))
        #print([int(200),int(1),Vlsb,Vmsb,Wlsb,Wmsb,cheacksum])

rospy.init_node('arduno_referencia')
sub = rospy.Subscriber("Arduino_reference",Twist,callback)

