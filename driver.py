#!/usr/bin/env python2.7

import RPi.GPIO as gpio
from time import sleep

from motor import Motor

gpio.setmode(gpio.BCM)

# Pins
left_a = 27
left_b = 22

right_a = 5
right_b = 6

left_motor = Motor(gpio, uid="left", pin_a=left_a, pin_b=left_b)
right_motor = Motor(gpio, uid="right", pin_a=right_a, pin_b=right_b)

for i in range(90):
	left_motor.forward()
	right_motor.forward()
	sleep(0.25)

left_motor.stop()
right_motor.stop()
sleep(1)

for i in range(90):
	left_motor.backward()
	right_motor.backward()
	sleep(0.25)

left_motor.stop()
right_motor.stop()

gpio.cleanup()
print "All done!"