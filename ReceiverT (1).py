import socket
import subprocess

port = 60000
#s = socket.socket();

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADRR, 1)

#host = socket.gethostname()
host = "196.47.235.71"
print(host)
s.bind(("", port))
s.listen(5)

print "Server listening..."

"""
while True:
	conn, addr = s.accept()
	print "got connection from", addr
	data = conn.recv(1024)
	print "Server received", repr(data)

	f = open("Binary", "rb")
	l = f.read(1024)

	while(l):
		conn.send(l)
		print "Sent ", repr(l) 
		l = f.read(1024)
	f.close()

	print "Done Sending"
	conn.send "Thank you for connecting" 
	conn.close()
"""


counter = 0;
while True:

	conn, addr = s.accept()
	print  "got connection from", addr 
	
        with open("ByteT", "wb") as f:
                print "file opened"
                while True:
                        print "receiving data..."
                        data = conn.recv(1024).decode()
                        #print "data=%s", (data)
                        if not data:
                                break
			
			print "data= ", data
                        f.write(data)
                        f.close()
                        counter = 1
			subprocess.call(["make"])
               
                print "Done Receiving" 
                conn.send("Thank you for connecting") 
                conn.close()

"""
while True:
	conn, addr = s.accept()
	data = conn.recv(1024)
	print(data)
"""
