import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

pinout = 18

GPIO.setup(pinout, GPIO.OUT)

f = 38000
dutycycle = 50

sleepTime = 0.0005625
#sleepTime = 0.0002

file = open("BinaryT", "r")
st = file.read()

print ("Sending data with command bits... \n")
print st

for i in range(0, len(st)):
	if st[i] != "":
		if int(st[i])==1:
			GPIO.output(pinout, GPIO.HIGH)
			time.sleep(sleepTime * 3)
			#GPIO.output(pinout, GPIO.LOW)
			#time.sleep(sleepTime)
			#GPIO.output(pinout, GPIO.HIGH)
			#time.sleep(sleepTime)
			GPIO.output(pinout, GPIO.LOW)
			time.sleep(sleepTime)
		elif int(st[i])==0:
			GPIO.output(pinout, GPIO.HIGH)
			time.sleep(sleepTime)
			GPIO.output(pinout, GPIO.LOW)
			time.sleep(sleepTime * 3)


#PWM.stop()
GPIO.cleanup()
