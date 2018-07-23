#!python3
#guessthenumber.py (version2) -> normal ifelse
#This program prompt the user to guess a number between 1 to 20, 6 tries given
#if user enters number above 20 or negatives, prompt user to enter within the range
#if user guessed right within 6 tries, display good job message; else, display secret number


import random
print('Hello. what is your name')
name = input()
secretnumber = random.randint(1,20)
print('Well, '+ name + ' ,I am thinking of a number between 1 to 20')

for numofguess in range(1,6):
    print('Take a guess')
    number = int(input())

    if secretnumber < number:
        print('Too high')
    elif secretnumber > number:
        print('Too low')
    else:
        break

if number == secretnumber:
    print('Good job, ' +name+ ' You guessed my number in '+numofguess)
elif number != secretnumber:
    print('Too bad. The number I was guessing was ' +str(secretnumber))