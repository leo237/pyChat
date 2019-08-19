#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
from termcolor import colored

#host = socket.gethostname() # Get local machine name
host = '192.168.1.6'

s = socket.socket()         # Create a socket object
print("Host : {}".format(host))
port = 12345              # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

name = raw_input("Enter your name:")

s.listen(5) 
c, addr = s.accept()                   # Now wait for client connection.
while True:
   rcv_message = c.recv(1024)  
   print(colored(rcv_message, 'green'))
   msg = raw_input("> ")
   c.send("{} : {}".format(name, msg))
c.close() 
