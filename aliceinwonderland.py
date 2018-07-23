import sys


print('Welcome to Wonderland')
while True:
    print('What is your name?')
    alice = input()
    if alice != 'Alice':
        print('Hi ' +alice+ '! We are not looking for you sadly. Bye now.')
        sys.exit()
    print('Hi Alice. What is the password?')
    password = input()
    if password == 'tea':
        print('Are you sure you are THE Alice?')
        while True:
            print('Can you slay the dragon?')
            dragon = input()
            if dragon == 'yes':
                print('You are THE Alice! We are in grave danger!')
                sys.exit()
            else:
                print('You are not THE Alice')
                print('I will ask this again.')
                continue