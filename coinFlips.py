#!python3
#This program displays calculated number of times of heads and tails came up

import random

heads = 0
tails = 1

for i in range(1,1001):
    if random.randint(0,1) == 1:
        heads = heads + 1
    if random.randint(0,1) == 0:
        tails = tails + 1
    if i == 500:
        print('Halfway done!')

print('Heads came up '+str(heads)+ ' times')
print('Tails came up '+str(tails)+ ' times')
