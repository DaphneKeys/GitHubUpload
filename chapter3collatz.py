#automate the boring stuff page 77 (Collatz Sequence)
#with try and except value error.

def collatz(number):
    if number % 2 == 0:
        return(number // 2)
    elif number % 2 == 1:
        return(3*number+1)

number = int(input("Give me a number: "))
while number != 1:
    number = collatz(number)
    print(number)
