#!/usr/bin/env/python3

# Script Name:                  Ops 401 - Challenge 37
# Author:                       Amleset Tesfamariam, CF Ops lecture 401, ChatGPT, https://github.com/codefellows/seattle-cybersecurity-401d10/tree/main/class-37/challenges 
# Date of latest revision:      02/27/2024
# Purpose:                      Using an existing Python script, add features that enables the user to capture a cookie and send it back out to the site in order to receive a valid response in HTTP text.
# Reason:                       It is vital to be able to identify and analyze user cookies to obtain essential information/data about the target.


# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
import webbrowser

targetsite = input("Enter target site:") # Uncomment this to accept user input target site
# targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')


def save_response_to_html(response_content):
    with open("response.html", "w") as html_file:
        html_file.write(response_content)

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# - Send the cookie back to the site and receive an HTTP response
response_with_cookie = requests.get(targetsite, cookies=cookie)

# - Generate a .html file to capture the contents of the HTTP response
save_response_to_html(response_with_cookie.text)

# - Open it with Firefox
webbrowser.open("response.html")



# Stretch Goal
# - Give Cookie Monster hands
