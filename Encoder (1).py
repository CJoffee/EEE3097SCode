import binascii
file = open("ByteT","r")
#file = open("StressFile", "r")

st = file.read()
file.close

stBin = bin(int(binascii.hexlify(st), 16))
stBin = stBin[2:]


counter0 = 0;
counter1 = 0;

for i in range (0, len(stBin)):
	if stBin[i] == "1":
		counter1 = counter1 + 1
	else:
		counter0 = counter0 + 1

bcounter0 = '{0:016b}'.format(counter0)
bcounter1 = '{0:016b}'.format(counter1)

stBin = stBin + bcounter0 + bcounter1


if stBin.endswith("0"):
	#stBin = "11111" + stBin + "1111111111"
	stBin = stBin + "11111111111111111111"
else:
	#stBin = "11111" + stBin + "0000000000"
	stBin = stBin + "00000000000000000000"

#print "String with header is: ", stBin

file = open("BinaryT", "w")
file.write(stBin);
file.close();
