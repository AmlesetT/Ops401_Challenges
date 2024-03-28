#!/usr/bin/python3

# Script Name:                  Ops 401 - Challenge 42
# Author:                       Amleset Tesfamariam, CF Ops lecture 401 & https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-42/challenges/DEMO.md, ChatGPT
# Date of latest revision:      03/27/2024
# Purpose:                      To develop a Python script custom for a Nmap scanner that can be used in combination with other scripts for pentesting.
# Reason:                       It can be very useful to combine tools and resources to help maximize efficiency and security, especially when scanning/searching for potential vulnerabilities.


import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you enetered is: ", ip_addr)

resp = input("""\nSelect scan to execute:
             1) SYN ACK Scan
             2) UDP Scan
             3) Comprehensive Scan\n""")

print("You have selected option: ", resp)

port_range = input("Enter port range (e.g., 1-100): ")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sS -sU -sV -O -A')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open TCP Ports: ", scanner[ip_addr]['tcp'].keys())
    print("Open UDP Ports: ", scanner[ip_addr]['udp'].keys())
else:
    print("Please enter a valid option")

