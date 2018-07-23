theboard = {'top-L' : ' ', 'top-M':' ','top-R' : ' ',
            'Center-L': ' ','Center-M': ' ', 'Center-R' : ' ',
            'Bottom-L':' ', 'Bottom-M':' ', 'Bottom-R':' ' }

def displayboard(board): #display the board
    print(board['top-L'] + '|' +board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['Center-L'] + '|' + board['Center-M'] + '|' + board['Center-R'])
    print('-+-+-')
    print(board['Bottom-L'] + '|' + board['Bottom-M'] + '|' + board['Bottom-R'])


user = 'O'
for turn in range(9):
    displayboard(theboard)
    print('Hi user. What is your move?')
    userO = input()
    theboard[userO] = user


computer = 'X'
for turn in range(9):
    displayboard(theboard)
    print('Computer moves')
    if userO in theboard['Center-M']:
        computer = theboard['Bottom-L']




displayboard(theboard) #parameter theboard to connect.