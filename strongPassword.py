#! python3
#strongPassword.py

#Strong Password Detection

import re

#Create a regex for password requirements
passwordRegex = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')

#Create a function - test if the password passed is strong
def password():
    print('Enter a password: ')
    userpassword = input()
    mo = passwordRegex.search(userpassword)
    if not mo:
        print('Password is not strong')

    else:
        print('Password is strong')


password()