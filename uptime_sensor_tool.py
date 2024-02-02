#!/usr/bin/python3

# Script Name:                  Ops 401 - Challenge 02
# Author:                       Amleset Tesfamariam, CF Ops lecture 401, ChatGPT
# Date of latest revision:      02/01/2024
# Purpose:                      To create a Python script including an uptime sensor tool to check for ICMP packets evaluating if hosts on the LAN are up or down.
# Reason:                       It is crucial to know how to use different tools to check and see whether systems are responding and furthermore, be able to track the status of critical infrastructures.


import os
import time
from datetime import datetime


def check_host_status(ip_address):
    response = os.system(f"ping -c 1 {ip_address} > /dev/null 2>&1")
    return response == 0

def main():
    destination_ip = "8.8.8.8"  # Change this to correct IP address to ping

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        success = check_host_status(destination_ip)

        if success:
            status = "Network Active"
        else: 
            status = "Network Inactive"

        print(f"{timestamp} {status} to {destination_ip}")

        time.sleep(2)
        print('Did I sleep for 2 seconds')


import os

result = os.system('ping localhost -c 2')



if __name__ == "__main__":
    main()


# End
