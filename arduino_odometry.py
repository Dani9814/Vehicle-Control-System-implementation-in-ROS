!/usr/bin/env python
import time
import rospy
import serial
import math
from geometry_msgs.msg import Twist
import numpy

pub = rospy.Publisher('vehicle_speed', Twist, queue_size=10)
msg=Twist() 
rospy.init_node('arduino_odometry')
ser = serial.Serial('/dev/ttyACM0',115200)
#print ser.read()
while True:
        #print(ser.inWaiting())
        if ser.inWaiting()>0: #si hay datos disponibles
                if 200==int(ser.read().encode('hex'), 16): #Cabecera del mensaje
                        #print('cabecera')
                        if 1==int(ser.read().encode('hex'), 16): #comprueba si es el tipo de 
                                #print('tipo')
                                suma=200+1
                                mensaje=numpy.zeros(5)
                                for i in range(0,5):
                                        mensaje[i]=int(ser.read().encode('hex'), 16)
                                        suma=suma+mensaje[i]
                                print(mensaje)
                                if suma%256==0:#Comprueba que se cumpla el cheacksum

                                        if mensaje[1]//128==1:
                                                signo1=-1
                                        else: 
                                                signo1=1
                                        if mensaje[3]//128==1:
                                                signo2=-1
                                        else: 
                                                signo2=1
                                        print('envio')
					msg.linear.x=signo1*((mensaje[1]%128)*2$
                                        msg.angular.z=signo2*((mensaje[3]%128)*$
                                        pub.publish(msg)
        else:
                #print 'no data'
                time.sleep(1)

rospy.spin()


