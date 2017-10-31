import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)

str='setinitial'

while str!= 'exit'


    str = raw_input()
    if str == 'on':
     print "LED on"
     GPIO.output(26,GPIO.HIGH)


    if str == 'off':
     print "LED off"
     GPIO.output(26,GPIO.LOW)
       
#by bhan    
