#!/usr/bin/python3

# Script Name:                  Ops 401 - Challenge 03
# Author:                       Amleset Tesfamariam, CF Ops lecture 401, ChatGPT, and Information from Medium (https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151)
# Date of latest revision:      02/02/2024
# Purpose:                      To existing Python script add capability to check systmes are responding by adding automated email feature that notifies you of any status changes.
# Reason:                       It is crucial to know how to use different tools to check and see whether systems are responding and furthermore, be able to track the status of critical infrastructures.


import os
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import sys


def check_host_status(ip_address):
    response = os.system(f"ping -c 1 {ip_address} > /dev/null 2>&1")
    return response == 0

def send_notification_email(sender_email, sender_password, receiver_email, host, status_before, status_after, timestamp):
    subject = "Host Status Change Notification"
    body = f"Host {host} status changed from {status_before} to {status_after} at {timestamp}"

    send_email(sender_email, sender_password, receiver_email, subject, body)

def send_email(sender_email, sender_password, receiver_email, subject, body):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def main():
    try:
        destination_ip = "8.8.8.8"  # Change this to correct IP address to ping
        sender_email = input("Enter your email address: ")
        if not sender_email:
            sender_email = 'username@gmail.com'  #Enter your unique email here
        sender_password = input("Enter your email password (App Password for Gmail): ")
        if not sender_password:
            sender_password = "password"  #Enter your unique password here
        receiver_email = input("Enter the administrator's email address: ")

        subject = "Test Notification"
        body = "This is a test email notification from your Python script."

        send_email(sender_email, sender_password, receiver_email, subject, body)

        print("Email was sent successfully.")
    except KeyboardInterrupt:
        exit("\nExiting the script")

    status_before = None

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        success = check_host_status(destination_ip)

        if status_before is None:
            status_before = "Netowrk Active" if success else "Network Inactive"
        else:
            status_after = "Network Active" if success else "Network Inactive"
            if status_before != status_after:
                send_notification_email(sender_email, sender_password, receiver_email, destination_ip, status_before, status_after, timestamp)
                status_before = status_after

        print(f"{timestamp} Network {'Active' if success else 'Inactive'} to {destination_ip}")
        
        time.sleep(2)
        print('Did I sleep for 2 seconds')

if __name__ == "__main__":
    main()


def exit(message='Thank you for using my script'):
    print(message)
    sys.exit()


# End
