#!/usr/bin/python3

# Script Name:                  Ops 401 - Challenge 26
# Author:                       Amleset Tesfamariam, CF Ops lecture 401, ChatGPT
# Date of latest revision:      02/12/2024
# Purpose:                      To create a Python script that incorporates logging capabilities.
# Reason:                       It is helpful to understand and be able to use logging tools to further detail, monitor, analyze, and track different events, actions, or activities that take place within a computer's system.


import ssl
import time
import paramiko
import getpass
import logging
import os
from zipfile import ZipFile

log = logging.getLogger("my_data_logger")

logging.basicConfig(filename='class26file.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

log.info("Hello, World")
log.warning("THIS IS A WARNING!")
log.error("THERE IS AN ERROR HERE:")

def do_something():
    log.debug("Attempting to do something, please wait.")

do_something()


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def get_words():
    downloads_folder = os.path.expanduser("~/Downloads")
    file_path = os.path.join(downloads_folder, "rockyou-70.txt")
    with open(file_path, 'r') as file:
        word_list = [line.strip() for line in file]
    return word_list

def check_for_word(words):
    user_answer = input("Enter a word: ")
    if user_answer in words:
        print("The word is in the dictionary")
    else:
        print("The word is not in the dictionary")

def load_external_file():
    password_list = []
    with open('rockyou-70.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.rstrip()
            password_list.append(line)
        print(password_list)

def get_host():
    host = input('Enter an SSH Client to connect to or enter for default: ') or "169.254.254.183"
    return host

def get_user():
    user = input("Enter a username or enter for default: ") or "Jim Sanders"
    return user

def get_password():
    password = getpass.getpass(prompt="Please provide a password:") or "Password123"
    return password

def ssh_client():
    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(get_host(), port, get_user(), get_password())
        stdin, stdout, stderr = ssh.exec_command("whoami")
        time.sleep(3)
        output = stdout.read()
        print("-" * 50)
        print(output)
        stdin, stdout, stderr = ssh.exec_command("ls -l")
        time.sleep(3)
        output = stdout.read()
        print(output)
        stdin, stdout, stderr = ssh.exec_command("uptime")
        time.sleep(3)
        output = stdout.read()
        print(output)
        print("-" * 50)
    
    except paramiko.AuthenticationException as e:
        print("Authentication Failed")
        print(e)

    finally:
        ssh.close()

def unzip_zip_file(zip_file_path, passwords):
    for password in passwords:
        try:
            with ZipFile(zip_file_path) as zf:
                zf.extractall(pwd=bytes(password, 'utf-8'))
            print(f"Successfully extracted with password: {password}")
            break #Break out of the loop if extraction is successful 
        except Exception as e:
            print(f"Failed with password: {password}")
            # Handle exception (e.g., incorrect password)


if __name__ == "__main__":
   external_words = get_words()
   unzip_zip_file("test1.zip", external_words)
    
    # zip -er test1.zip test1.txt
    # external_words = get_words()
    # print(external_words)
    # print(word_list)
    # check_for_word(external_words)
    # load_external_file()
    # ssh_client()

# End
