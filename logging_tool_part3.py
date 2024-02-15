#!/usr/bin/python3

# Script Name:                  Ops 401 - Challenge 28
# Author:                       Amleset Tesfamariam, CF Ops lecture 401, ChatGPT, https://realpython.com/python-logging/#using-handlers 
# Date of latest revision:      02/14/2024
# Purpose:                      To existing Python script which includes logging capabilities and log rotation feature based on size, add streamhandler (output to terminal) and filehandler (output to local file).
# Reason:                       It is helpful to understand and be able to use logging tools to further detail, monitor, analyze, and track different events, actions, or activities that take place within a computer's system.


import ssl
import time
import paramiko
import getpass
import logging
import os
from zipfile import ZipFile
from logging.handlers import RotatingFileHandler
from logging import StreamHandler

log_file = 'class26file.log'
max_log_size = 1024 * 1024 * 5
backup_count = 3
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler = RotatingFileHandler(log_file, maxBytes=max_log_size, backupCount=backup_count)
file_handler.setFormatter(formatter)

stream_handler = StreamHandler()
stream_handler.setFormatter(formatter)

log = logging.getLogger()
log.addHandler(file_handler)
log.addHandler(stream_handler)

log.setLevel(logging.DEBUG)

log.info("Hello, World")
log.warning("THIS IS A WARNING!")
log.error("THERE IS AN ERROR HERE:")

def do_something():
    log.debug("Attempting to do something, please wait.")

do_something()


try:
    ssl._create_default_https_context = ssl._create_unverified_context
except AttributeError:
    pass


def get_words():
    file_path = os.path.expanduser("~/Downloads/rockyou-70.txt")
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def get_host():
    return input('Enter an SSH Client to connect to or enter for default: ') or "169.254.254.183"

def get_user():
    return input("Enter a username or press enter for default: ") or "Jim Sanders"

def get_password():
    return getpass.getpass(prompt="Please provide a password:") or "Password123"

def ssh_client():
    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(get_host(), port, get_user(), get_password())
        for cmd in ["whoami", "ls -l", "uptime"]:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            time.sleep(3)
            output = stdout.read()
            print("-" * 50)
            print(output)
        print("-" * 50)
    except paramiko.AuthenticationException as e:
        print("Authentication Failed")
        print(e)
        log.error("Authentication failed: %s", e)
    finally:
        ssh.close()


def unzip_zip_file(zip_file_path, passwords):
    for password in passwords:
        try:
            with ZipFile(zip_file_path) as zf:
                zf.extractall(pwd=bytes(password, 'utf-8'))
            print(f"Successfully extracted with password: {password}")
            log.info("Successfully extracted with password: %s", password)
            break   #Break out of the loop if extraction is successful 
        except Exception as e:
            print(f"Failed with password: {password}")
            log.error("Failed with password: %s, error: %s", password, e)

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
