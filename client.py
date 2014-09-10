#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
#host = "192.168.1.38"
port = 12345   

s.connect((host, port))
while True:
	msg = raw_input("Message:")
	s.send(msg)
	print "server:", s.recv(1024)
s.close


# To find sockets that haven't been closed properly, execute the following
# ps -fA | grep python 
# Then kill all the unwanted sockets. Ciao.