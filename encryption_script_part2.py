#!/usr/bin/python3

# Script Name:                  Ops 401 - Challenge 07
# Author:                       Amleset Tesfamariam, CF Ops lecture 401, ChatGPT
# Date of latest revision:      02/04/2024
# Purpose:                      To existing Python script add feature that recursively encrypts and decrypts single folder and its contents.
# Reason:                       It is important to understand how to encrypt data at different stages, including data at rest.

import os
for root, dirs, files in os.walk("."):
    print(root)
    print(dirs)
    print(files)
    for file in files:
        with open(file) as f:
            print(f.read())
    print('-' * 80)


from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_file_path = file_path + ".encrypted"
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_data = f.encrypt(data)
        encrypted_file.write(encrypted_data)

    os.remove(file_path)
    print("File encrypted successfully.")
    
def decrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_file_path = file_path[:-10]
    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_data = f.decrypt(encrypted_data)
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
            file_path = input("Enter the file or folder path: ")
            if not os.path.exists(file_path):
                print("Path not found. Please provide a valid file or folder path.")
                continue

            if mode == "1":
                if os.path.isfile(file_path):
                    encrypt_file(file_path, key)
                    print("Encryption completed.")
                elif os.path.isdir(file_path):
                    encrypt_folder(file_path, key)
                print("Recursive encryption completed.")


            elif mode == "2":
                if os.path.isfile(file_path):
                    decrypt_file(file_path, key)
                    print("Decryption completed.")
                elif os.path.isdir(file_path):
                    decrypt_folder(file_path, key)
                print("Recursive decryption completed.")

        elif mode == "3":
            cleartext = "Hello friend, welcome to cybersecurity!"
            encrypt_string(cleartext, key)

        elif mode == "4":
            ciphertext = input("Enter the ciphertext string: ")
            decrypt_string(ciphertext, key)


# End
