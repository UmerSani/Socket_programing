import socket
import sys
from thread import *

def read(s):
	while True:
		data=recv(1024)
		print(data)

               # Import socket module

s = socket.socket()         
host = socket.gethostname()
port = 5188                # Reserve a port for your service.
s.connect((host, port))
#name=input("Enter your Name\n")
s.sendall("sanii")
cname=input("Enter Your Friend name \n")
s.sendall(cname)
data=s.recv(4096)
print ('list  :-',str(data))
while (1):
	data=s.recv(1024)
	if data=='connected':
		break
	else:
		data=s.recv(1024)
		s.sendall(data)

start_new_thread(read,(s,))
while True:
	data=input()
	s.sendall(data)
s.close()
                    # Close the socket when done

def fun(s):
	
	while True:
		data=raw_input()
		if not data:
			break
		else:
			s.sendall(data)
			data=s.recv(1024)
			if not data:
				break
			else:
				print data
	s.close()
