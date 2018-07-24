import random
print('Whatis your name?')
name = input()
while True:
    print('Hello! ' + name + ' We are going to play a guess game. Choose a number between 1 to 20')
    answer = random.randint(1,20)
    guessestaken = 0
    while guessestaken != 4:
        while True:
            guess = input('Take a guess : ')
            try:
                guess= int(guess) #int for user input
                break
            except ValueError: #when error is ValueError, print the following then return to While True
                print('you did not type number') 

        if guess > answer:
            print('That is too high')
            guessestaken += 1 #increment guessestaken for every guess
        elif guess < answer:
            print('That is too low')
            guessestaken += 1
        else:
            break
    if guess == answer:
        print('Yes, that is correct, It was ' + str(answer) +'!  You have tried ' + str(guessestaken) + ' times out of 4')
        break
    else:
        print('Oh no... You have tried ' + str(guessestaken) + ' times out of 4, the correct answer was ' + str(answer))
        break


#works. send this answer later.
