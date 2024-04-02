#!/usr/bin/python3

# Script Name:                  Ops 401 - Challenge 12
# Author:                       Amleset Tesfamariam, CF Ops lecture 401, https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-12/challenges/DEMO.md, ChatGPT
# Date of latest revision:      04/01/2024
# Purpose:                      To existing network scanning tool using Python library Scapy, add features including: ICMP ping sweep tool.
# Reason:                       It can be extremely helpful to create scanning tools that are customizable which increase efficiency, time, and resources.


# pip install scapy

import ipaddress
from scapy.all import *

def scan_port(host, port):
    response = sr1(IP(dst=host) / TCP(dport=port, flags="S"), timeout=1, verbose=0)

    if response is None:
        print(f"Port {port} is filtered and silently dropped.")
    elif response.haslayer(TCP):
        if response[TCP].flags == 0x12:
            # Send RST packet to close the connection
            send(IP(dst=host) / TCP(dport=port, flags="R"), verbose=0)
            print(f"Port {port} is open.")
        elif response[TCP].flags == 0x14:
            print(f"Port {port} is closed.")
        else:
            print(f"Port {port} has an unknown response.")
    else:
        print(f"Port {port} has an unknown response.")

def scan_ports(host, port_range):
    for port in port_range:
        scan_port(host, port)

def icmp_ping_sweep(network):
    hosts_online = 0
    for ip in ipaddress.IPv4Network(network).hosts():
        if ip == ip.network or ip == ip.broadcast:
            continue
        response = sr1(IP(dst=str(ip))/ICMP(), timeout=1, verbose=0)
        if response is None: 
            print(f"Host {ip} is down or unresponsive.")
        elif response.haslayer(ICMP) and response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
            print(f"Host {ip} is actively blocking ICMP traffic.")
        else:
            print(f"Host {ip} is responding.")
            hosts_online += 1
    print(f"Total {hosts_online} hosts are online.")

if __name__ == "__main__":
    choice = input("Choose mode: \n1. TCP Port Range Scanner mode \n2. ICMP Ping Sweep mode \nEnter your choice (1/2): ")
    if choice == "1":
        host = input("Enter the host IP: ")
        port_range = input("Enter the port range (start-end): ").split("-")
        port_range = range(int(port_range[0]), int(port_range[1])+1)
        scan_ports(host, port_range)
    elif choice == "2":
        network = input("Enter the network address including CIDR block (e.g., '10.10.0.0/24'): ")
        icmp_ping_sweep(network)
    else:
        print("Invalid choice.")

# End 
