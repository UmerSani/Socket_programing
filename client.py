
import socket               # Import socket module

s = socket.socket()         
host = socket.gethostname()
port = 5188                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
while True:
	data=raw_input()
	if not data:
		break
	else:
		s.sendall(reply)
		data=s.recv(1024)
		if not data:
			break
		else:
			print data
s.close                     # Close the socket when done
