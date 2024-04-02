#!/usr/bin/python3

# Script Name:                  Ops 401 - Challenge 11
# Author:                       Amleset Tesfamariam, CF Ops lecture 401, https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-11/challenges/demo.py, ChatGPT
# Date of latest revision:      04/01/2024
# Purpose:                      To develop a customizable network scanning tool using Python library Scapy.
# Reason:                       It can be extremely helpful to create scanning tools that are customizable which increase efficiency, time, and resources.


# pip install scapy

from scapy.all import Ether, IP, sniff, ARP, sr1, ICMP, TCP

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

if __name__ == "__main__":
    host = 'scanme.nmap.org' # Select the host IP
    port_range = range(1, 1001) # Select the port range to scan
    scan_ports(host, port_range)

# End 
