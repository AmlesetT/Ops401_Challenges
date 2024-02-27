#!/usr/bin/python3

# Script Name:                  Ops 401 - Challenge 36
# Author:                       Amleset Tesfamariam, CF Ops lecture 401, ChatGPT
# Date of latest revision:      02/26/2024
# Purpose:                      To develop a Python script that utilizes multiple banner grabbing or service fingerprinting aproaches against a single targeted system.
# Reason:                       It is helpful to understand how a system can be targeted such as fingerprinting techniques to gain valueable information regarding the targeted system.


#Option 1 for banner grabbing using netcat:

import subprocess

def banner_grabbing():
    #Prompt user for targeted URL or IP address
    target_address = input("Please enter the targeted URL or IP address: ")

    #Prompt user for targeted port number
    port_number = input("Please enter the targeted port number: ")

    #Execute netcat command to perform targeted banner grabbing
    try: 
        #Run netcat command and capture output
        result = subprocess.run(['nc', '-v', '-n', '-z', '-w', '2', target_address, port_number], capture_output=True, text=True, timeout=5)

        #Print the result
        print(result.stdout)

    except subprocess.TimeoutExpired:
        print("Connection timed out.")

if __name__ == "__main__":
    banner_grabbing()


#Option 2 for banner grabbing using telnet:

import telnetlib

def banner_grabbing():
    #Prompt user for targeted URL or IP address
    target_address = input("Please enter the targeted URL or IP address: ")

    #Prompt user for targeted port number
    port_number = input("Please enter the targeted port number: ")

    try:
        #Execute connection using telnet to targeted address and port
        tn = telnetlib.Telnet(target_address, port_number, timeout=5)
        
        #Receive grabbed banner message
        banner = tn.read_until(b"\n", timeout=5).decode("utf-8")

        #Print the received banner message
        print("Banner message: ")
        print(banner)

        #Close the telnet connection
        tn.close()

    except ConnectionRefusedError:
        print("Connection refused.")
    except TimeoutError:
        print("Connection timed out.")
    except Exception as e:
        print("An error has occurred:", e)

if __name__ == "__main__":
    banner_grabbing()


#Option 3 for banner grabbing using nmap:

    #pip install python-nmap        (Ensure nmap is installed)

import nmap 

def banner_grabbing():
    #Prompt user for targeted URL or IP address
    target_address = input("Please enter the targeted URL or IP address: ")

    #Initialize nmap portscanner object
    nm = nmap.PortScanner()

    #Prompt user for targeted port number
    port_number = input("Please enter the targeted port number (or press enter for known default port numbers): ")

    if port_number:
        #Perform targeted banner grabbing on the specified port
        nm.scan(target_address, arguements=f'-p {port_number} --open -sV')
    
    else:
        #Perform targeted banner grabbing on known default ports (1-1024)
        nm.scan(target_address, arguments='-p1-1024 --open -sV')

    #Print nmap scan results
    for host in nm.all_hosts():
        print(f"Host: {host}")
        for port in nm[host]['tcp']:
            print(f"Port {port}: {nm[host]['tcp'][port]['product']} {nm[host]['tcp'][port]['version']}")

if __name__ == "__main__":
    banner_grabbing()

