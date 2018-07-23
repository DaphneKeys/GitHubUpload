def collatz(number):
    while number > 1:
        if number % 2 == 0:
            return (number // 2)  # even number
        else:
            return (3 * number + 1)  # odd number
