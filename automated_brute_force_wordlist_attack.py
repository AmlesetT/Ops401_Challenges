#!/usr/bin/python3

# Script Name:                  Ops 401 - Challenge 16
# Author:                       Amleset Tesfamariam, CF Ops lecture 401, ChatGPT
# Date of latest revision:      01/29/2024
# Purpose:                      To create a script that prompts the user to select Mode 1: Offensive; Dictionary Iterator, or Mode 2: Defensive; Password Recognized.
# Reason:                       It is important to know how to recognize, analyze, and appropriately use automated brute force wordlist attack tools, to better defend systems.



import ssl
import rockyou-70
from rockyou-70.txt import words

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def get_words():
    rockyou-70.txt.download('words')
    word_list = words.words()
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

if __name__ == "__main__":
    external_words = get_words()
    # print(external_words)
    # print(word_list)
    # check_for_word(external_words)
    load_external_file()



# End