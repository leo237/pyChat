#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
from termcolor import colored

host = "192.168.1.6"
#host = socket.gethostname() # Get local machine name

s = socket.socket()         # Create a socket object
print("Host : {}".format(host))
port = 12345   

name = raw_input("Enter your name :")

s.connect((host, port))
while True:
        msg = raw_input("> ")
        s.send("{} : {}".format(name, msg))
        print(colored(s.recv(1024), 'green'))
s.close


# To find sockets that haven't been closed properly, execute the following
# ps -fA | grep python 
# Then kill all the unwanted sockets. Ciao.
