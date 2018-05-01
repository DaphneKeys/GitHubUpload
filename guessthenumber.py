import random
print('Hello. what is your name')
name = input()
secretnumber = random.randint(1,20)
print('Well, '+ name + ' ,I am thinking of a number between 1 to 20')

for guesses in range(1,7): #guess 6 times
    print('Take a guess')
    number = int(input())

    if secretnumber < number:
        print('Too high')
        if number >= 21: #if number is more than 20
            print('I am thinking between 1 to 20')
    elif secretnumber > number:
        print('Too low')
        if number <= -1: #if number is negative
            print('No negative number. I am thinking between 1 to 20')
    else:
        print('you guessed right. I was thinking of ' + str(secretnumber))
        break
if number == secretnumber:
    print('Good job, ' +name+ ' .You guessed my number in '+str(guesses))
elif number != secretnumber:
    print('Too bad. The number I was thinking of is ' +str(secretnumber))


