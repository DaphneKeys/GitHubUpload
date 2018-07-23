# while Loop
spam = 0
while spam < 5:
    print('Hello world!')
    spam = spam + 1
print('Example 1')
print('-'*13)

#Repeats until user type in 'your name'
name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')
print('Example 2')
print('-'*13)

#infinite loop with break
name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        print('Thank you!')
        break
print('Example 3')
print('-'*13)
#continue statement
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3: #jumps back to the previous while loop
        continue
    print('spam is '+str(spam))
    print('Thank you!')
    break
print('Example 4')
print('-'*13)

#for loop
print('My name is')
for i in range(5): #i is set to 0
    print('Jimmy five times '+str(i))
print('Example 5')
print('-'*13)

total = 0
for num in range(101):
    total = total + num
print(total)
print('Example 6')
print('-'*13)

#nested loops
#for [first iterating variable] in [outer loop]:
#    [do something] #optional
#    for [second iterationg variable] in [nested loop]:
#        [do something]


#enumerate()
num_list = [1,2,3]
alpha_list = ['a','b','c']

for number in num_list:
    print(number)
    for letter in alpha_list:
        print(letter)

print('-'*13)

example = ['left', 'right','up','down']

for i in range(len(example)):
    print(i, example[i])

print('-'*13)

for i, j in enumerate(example):
    print(i,j)

new_dictionary = dict(enumerate(example))
print(new_dictionary)
