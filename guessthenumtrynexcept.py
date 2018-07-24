import random
print('What is your name?')
name = input()

while True: #infinite loop
    answer = random.randint(1,20)
    tries = 5 #added tries variable to count down works properly
    print('Hello! ' + name + ' We are going to play a guess game. Choose a number between 1 to 20\nTotal : 5 tries\n')
    while tries != 0: 
        while True:    
            guess = input('Take a guess: ')
            try:
                guess = int(guess)
                break
            except ValueError:
                print('Enter a number!')
        if guess > answer:
            tries -=1
            print('That is too high! Tries left :' +str(tries))
        elif guess < answer:
            tries -=1
            print('That is too low. Tries left : '+str(tries))
        else:
            break
        
    if guess == answer:
        print('Yes, that is correct, It was ' + str(answer) +'!  Tries left:' + str(tries) )
        break
    else:
        print('Oh no... You have 0 tries left, the correct answer was ' + str(answer))
        break
            

            
#Try and except works
#Everything works!
    
    
