#tic-tac-toe that *displays* X or O :- use top-L, top-M, top-R, mid-L, mid-M, mid-R, low-L, low-M, low-R

board = {'top-L' : ' ', 'top-M' : ' ', 'top-R':' ',
         'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
         'low-L' : ' ', 'low-M' : ' ', 'low-R': ' '}

def printboard(leboard):
    print(leboard['top-L']+ '|' + leboard['top-M']+ '|' + leboard['top-R'])
    print('-+-+-')
    print(leboard['mid-L'] + '|' + leboard['mid-M']+'|' + leboard['mid-R'])
    print('-+-+-')
    print(leboard['low-L']+'|' + leboard['low-M']+'|' + leboard['low-R'])

turn = 'X'
for i in range(9):
    printboard(board)
    print('Player ' +turn+ ' , move to which space?')
    move = input()
    board[move] = turn
    if turn == 'X':
         turn = '0'
    else:
         turn = 'X'

printboard(board)

