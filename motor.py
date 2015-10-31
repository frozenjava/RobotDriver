#
# Josh Artuso
# motor.py
#
# This object represents a motor to control
# I'm still new to this wonderful land of robotics but this is fun.
#

from time import sleep


class Motor:

	def __init__(self, gpio, uid=None, pin_a=None, pin_b=None):
		"""
		Constructor for the Motor object
		:param uid: The unique identifer for this motor
		:param pin_a: The pin to move the motor forward
		:param pin_b: The pin to move the robot backward
		"""
		self.FORWARD_PIN = pin_a
		self.BACKWARD_PIN = pin_b
		self.MOTOR_ID = uid
		self.gpio = gpio

		self.FAST = 0.0
		self.MEDIUM = 0.25
		self.SLOW = 0.75

		self.gpio.setup(self.FORWARD_PIN, self.gpio.OUT)
		self.gpio.setup(self.BACKWARD_PIN, self.gpio.OUT)

	def forward(self, speed=0.0):
		"""
		This method will move the motor forwards
		:param speed: The speed at which to move
		"""
		self.gpio.output(self.FORWARD_PIN, self.gpio.HIGH)
		sleep(speed)
		#self.stop()

	def backward(self, speed=0.0):
		"""
		This method will move the motor backwards
		:param speed: The speed at which to move
		"""
		self.gpio.output(self.BACKWARD_PIN, self.gpio.HIGH)
		sleep(speed)
		#self.stop()

	def stop(self):
		"""
		Stop the motor
		"""
		self.gpio.output(self.FORWARD_PIN, self.gpio.LOW)
		self.gpio.output(self.BACKWARD_PIN, self.gpio.LOW)