import binascii
import subprocess

file = open("BinaryR", "r")
content = file.read()
#content = "0b"+content

bcounter1 = content[-16:]
content = content[:-16]
bcounter0 = content[-16:]
content = content[:-16]

dataCorrect = 0

print "Actual: \n"
print bcounter0, "\n"
print bcounter1, "\n"

counter0 = 0
counter1 = 0

for i in range(0, len(content)):
	if content[i] == "1":
		counter1 = counter1 + 1
	elif content[i] == "0":
		counter0 = counter0 + 1

if(counter0 == int(bcounter0, 2) and counter1 == int(bcounter1, 2)):
	print "Number of zero: ", counter0, " ", int(bcounter0, 2)
	print "Number of one:", counter1, " ", int(bcounter1, 2)
	print "Data OK"
	dataCorrect = 1
else:
	print "Number of zero: ", counter0, " ", int(bcounter0, 2)
	print "Number of one:", counter1, " ", int(bcounter1, 2)
	print "Data Error"

content = "0b"+content
st = int(content, 2)
output = binascii.unhexlify("%x"%st)
print(output)

if(dataCorrect == 1):
	volume = output[0:3]
	audio = output[3:]

	subprocess.call(["amixer", "set", "PCM", "__", volume+"%"])
	#subprocess.call(["java", "-cp", ".:./jars/jfugue.jar", "MusicPlayer", audio])

f = open("ByteR", "w")
f.write(output)
f.close
