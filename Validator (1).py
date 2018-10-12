f1 = file("BinaryT", "r")
f2 = file("BinaryR", "r")

s1 = f1.read()
#s1  = s1[5:]
s1  = s1[:-20]
s2 = f2.read()

if s1 == s2:
	print("Validation passed")
else:
	print("Validation failed")

counter = 0

for i in range (len(s1)):
	if s1[i]!=s2[i]:
		print "Error at bit ", i, "; Expect ", s1[i], "; Got ", s2[i]
		counter = counter + 1

print "Total Length:", len(s1)
print "Error bits:", counter
print "BER: ", float(counter)/float(len(s1))
