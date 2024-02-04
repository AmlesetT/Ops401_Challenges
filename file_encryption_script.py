#!/usr/bin/python3

# Script Name:                  Ops 401 - Challenge 06
# Author:                       Amleset Tesfamariam, CF Ops lecture 401, ChatGPT
# Date of latest revision:      02/04/2024
# Purpose:                      To create a Python script that utilizes the cryptography library to encrypt a file (mode 1), decrypt a file (mode 2), encrypt a message (mode 3), and decrypt a message (mode 4). Depending on the selection perform certain functions.
# Reason:                       It is important to understand how to encrypt data at different stages, including data at rest.

import os
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted_data = f.encrypt(data)

    encrypted_file_path = file_path + ".encrypted"
    with open(file_path + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    os.remove(file_path)
    print("File encrypted successfully.")
    
def decrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = f.decrypt(encrypted_data)

    decrypted_file_path = file_path[:-10]
    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    os.remove(file_path)
    print("File decrypted successfully.")

def encrypt_string(cleartext, key):
    f = Fernet(key)
    message = cleartext.encode()
    encrypted = f.encrypt(message)
    print("Ciphertext is " + encrypted.decode('utf-8'))

def decrypt_string(ciphertext, key):
    f = Fernet(key)
    decrypted = f.decrypt(ciphertext.encode())
    print("Decrypted text is: " + decrypted.decode('utf-8'))

if __name__ == "__main__":
    write_key()
    key = load_key()


    while True:
        print("\nSelect a mode:")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Encrypt a message")
        print("4. Decrypt a message")
        print("0. Exit")

        mode = input("Enter mode (0-4): ")

        if mode == "0":
            break

        if mode in ["1", "2"]:
            file_path = input("Enter the file path: ")
            if not os.path.isfile(file_path):
                print("File not found. Please provide a valid file path.")
                continue

            if mode == "1":
                encrypt_file(file_path, key)

            elif mode == "2":
                decrypt_file(file_path, key)

        elif mode == "3":
            cleartext = "Hello friend, welcome to cybersecurity!"
            encrypt_string(cleartext, key)

        elif mode == "4":
            ciphertext = input("Enter the ciphertext string: ")
            decrypt_string(ciphertext, key)


# End
