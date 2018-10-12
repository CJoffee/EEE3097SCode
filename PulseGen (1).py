import pigpio
import sys

pi = pigpio.pi()
if not pi.connected:
	exit()

pi.hardware_PWM(12, 38000, 500000)
