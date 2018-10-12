import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

pinin = 23

GPIO.setup(pinin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#sleepTimeHigh = 0.001
#sleepTimeLow0 = 0.001
#sleepTimeLow1 = 0.003

sleepTime = 0.0005625
#sleepTime = 0.0002

while True:

	string = ""
	sensor = ""

	"""
	print("Waiting for initiating signal...")

	while(sensor != "11111"):

		if len(sensor) == 5:
			sensor = sensor[1:]

		if GPIO.input(pinin) == 1:
			time.sleep(sleepTime * 1.5)

			if GPIO.input(pinin) == 0:
				#if len(sensor)==5:
				#	sensor = sensor[1:]
				sensor = sensor + "0"
			elif GPIO.input(pinin) == 1:
				#if len(sensor)==5:
				#	sensor = sensor[1:]
				sensor = sensor + "1"

			time.sleep(sleepTime * 2)
			print sensor

	print("sensor is: " + sensor)
	sensor = ""

	print("Initiating signal received, waiting for data...")

	"""
	while(sensor != "11111111111111111111" and sensor != "00000000000000000000"):

		if len(sensor) == 20:
			sensor = sensor[1:]

		if GPIO.input(pinin) == 1:
			time.sleep(sleepTime * 1.5)

			if GPIO.input(pinin) == 0:
				string = string + "0"
				sensor = sensor + "0"
			elif GPIO.input(pinin) == 1:
				string = string + "1"
				sensor = sensor + "1"

			time.sleep(sleepTime * 2)

		#print(string)

	string = string[:-20]
	print ("Data Received: \n")
	print(string)

	file = open("BinaryR", "w")
	file.write(string)
	file.close()
	print("File written successfully")

	string = ""
	sensor = ""
	subprocess.call(["make", "decode"])
