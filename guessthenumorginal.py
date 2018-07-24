import random
print('Whatis your name?')
name = input()
print('Hello! ' + name + ' We are going to play a guess game. Choose a number between 1 to 20')
answer = random.randint(1,20)
for guessestaken in range(1,5):
    try:
        print('take a guess')
        guess= int(input()) #int for user input
    except ValueError: #except ValueError
        print('you did not type number')
        continue
    
    if guess > answer:
        print('That is too high')
    elif guess < answer:
        print('That is too low')
    else:
        break
if guess == answer:
    print('Yes, that is correct, It was ' + str(answer) +'!  You have tried ' + str(guessestaken) + ' times out of 4')
else:
    print('Oh no... You have tried ' + str(guessestaken) + ' times out of 4, the correct answer was ' + str(answer))
#original 
