#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
lol = ''
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345              # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5) 
c, addr = s.accept()                   # Now wait for client connection.
while lol != 'exit':
   lol = c.recv(1024)  
   print addr , ": " , lol
   msg = raw_input("Message:")
   c.send(msg)
c.close() 