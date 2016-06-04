import socket
import sys
from thread import *



               # Import socket module

s = socket.socket()         
host = socket.gethostname()
port = 5188                # Reserve a port for your service.
s.connect((host, port))
name=raw_input("Enter your Name\n")
s.sendall(name)

data=s.recv(4096)
print 'list is:-', str(data)

cname=raw_input("Enter Your Friend name \n")
s.sendall(cname)



while 1:
	data=s.recv(1024)
	if data=='connected':
		break
	else:
		data=s.recv(1024)
		s.sendall(data)


def read(s):
	while True:
		data=s.recv(1024)
		print data

start_new_thread(read,(s,))
while True:
	data=raw_input()
	s.sendall(data)
s.close()
                    # Close the socket when done


