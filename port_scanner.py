#!/usr/bin/python3

# Script Name:                  Ops 401 - Challenge 43
# Author:                       Amleset Tesfamariam, CF Ops lecture 401, ChatGPT
# Date of latest revision:      03/23/2024
# Purpose:                      To develop a Python script that determines if a target port is open or closed using Python 3 commands.
# Reason:                       It is helpful to understand which ports within a system are being used and furthermore, which resources are being used on the network.


#!/usr/bin/python3

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 10 #Done: Set a timeout value here.
sockmod.settimeout(timeout)

hostip = input("Enter the host IP: ") #Done: Collects a host IP from the user.
portno = int(input("Enter the port number: ")) #Done: Collects a port number from the user, then convert it to an integer data type.

def portScanner(portno):
    if sockmod.connect_ex((hostip, portno)) == 0:  #Done: Replaced "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
        print("Port Open")
    else:
        print("Port Closed")

portScanner(portno)

