#automate the boring stuff page 77 (Collatz Sequence)
#use try and except.

def collatz(number):
    if number % 2 == 0:
        return(number//2) #even number
    else:
        return(3*number+1) #odd number
try:
    number = int(input('Enter number'))
    while number != 1:
        number = collatz(number)
        print(number)
except ValueError:
    print('Enter number only, not string')


