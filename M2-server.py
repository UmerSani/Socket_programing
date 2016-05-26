'''
    Simple socket server using threads
'''
 
import socket
import sys
from thread import *
global name
global lst
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5188 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
    # conn1.send('Welcome to the server. Type something and hit enter\n')
    #infinite loop so that function do not terminate and thread do not end.
    k=True
    sname=conn.recv(1024)
    while k:
        #Receiving from client
        
	if sname  in name:
		conn.sendall('Connected ')
		temp=namearry[name]['index']
		lst[temp].sendall('Connected ')
		k=False
	elif k:
		conn.sendall('Enter name is Wrong')
		k=False
	else:
		data=conn.recv(1024)
		print('hehehe')
	while 1:
		data=conn.recv(1024)
		lst[temp].sendall(data)
		print (data)
	     
    #came out of loop
    conn.close()
i=0
#now keep talking with the client
name=[]
lst=[]
namearry=dict()
while 1:
	
    	#wait to accept a connection - blocking call
    	conn, addr = s.accept()
    	
	
    	print 'Connected with ' + addr[0] + ':' + str(addr[1])
    	lst.append(conn)
    	name=str(conn.recv(1024))
	namearry[name]={'index':i}
	i=i+1
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    
	start_new_thread(clientthread, (conn,))
 
s.close()
