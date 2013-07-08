#!/usr/bin/python
import RPi.GPIO as GPIO
import time

print 'start gpio raspberry'
 
GPIO.setmode(GPIO.BCM)
RED_LED = 23
GPIO.setup(RED_LED, GPIO.OUT)
 
while True:
	print 'Encendiendo led...',RED_LED
	GPIO.output(RED_LED, True)
	time.sleep(1)
	print 'Apagando led...',RED_LED
	GPIO.output(RED_LED, False)
	time.sleep(1)
