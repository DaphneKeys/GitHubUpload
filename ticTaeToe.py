### PLEASE SOLVE THIS IN THE FUTURE.
import random

board = {'top-L' : ' ', 'top-M' : ' ', 'top-R':' ',
         'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
         'low-L' : ' ', 'low-M' : ' ', 'low-R': ' '}

def theboard(leboard):
    print(leboard['top-L']+ '|' + leboard['top-M']+ '|' + leboard['top-R'])
    print('-+-+-')
    print(leboard['mid-L'] + '|' + leboard['mid-M']+'|' + leboard['mid-R'])
    print('-+-+-')
    print(leboard['low-L']+'|' + leboard['low-M']+'|' + leboard['low-R'])

def playerXorO():
    Xor0 = ''
    while not (Xor0 == 'X' or Xor0 == '0'):
        print('Do you want to be X or 0?')
        Xor0 = input()

    if Xor0 == 'X':
        return ['X', '0'] #FIRST ELEMENT IS PLAYER SECOND IS COMPUTER
    else:
        return ['0' , 'X']

def whofirst():
    #coin = {}
    #while coin not in ('heads', 'tails'):
    #    print('heads or tails')
    #    coin = input()
    #    flipthecoin = random.randint(0,1)
    #    if flipthecoin == coin:
    #        print('You go first')
    #    elif flipthecoin != coin:
    #        print('Computer first') #rmb to print lets begin after printing whofirst
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
def makeMove(leboard,Xor0, moveXor0):
    leboard[moveXor0] = Xor0

def winner(bo, le):
    return ((bo['top-L'] == le and bo['top-M'] == le and bo['top-R'] == le) or  # across the top
    (bo['mid-L'] == le and bo['mid-M'] == le and bo['mid-R'] == le) or  # across the middle
    (bo['low-L'] == le and bo['mid-M'] == le and bo['low-R'] == le) or  # across the bottom
    (bo['top-L'] == le and bo['mid-L'] == le and bo['low-L'] == le) or  # down the left side
    (bo['top-M'] == le and bo['mid-M'] == le and bo['low-M'] == le) or  # down the middle
    (bo['top-R'] == le and bo['mid-M'] == le and bo['low-R'] == le) or  # down the right side
    (bo['top-L'] == le and bo['mid-M'] == le and bo['low-R'] == le) or  # diagonal
    (bo['top-R'] == le and bo['mid-M'] == le and bo['low-L'] == le)) # diagonal

def getboardcopy(leboard):
    dupeboard = []

    for i in board:
        dupeboard.append(i)

    return dupeboard

def isSpaceFree(leboard, makeMove):
    return leboard[makeMove] == ' '

def getPlayerMove(leboard):
    move = ' '
    while move not in ('top-L','top-M', 'top-R','mid-L','mid-M','mid-R','low-L','low-M','low-R'):
        print('What is your next move?')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board,movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

def getComputerMove(leboard, computerLetter):
    if computerLetter == 'X':
        playerLetter = '0'
    else:
        playerLetter = 'X'

        #THE ALGORITHM FOR TIC TAC TOE
        #check if we can win in the next move
        for i in range(1,10):
            copy = getboardcopy(leboard)
            if isSpaceFree(copy, i ):
                makeMove(copy, computerLetter, i)
                if winner(copy, computerLetter):
                    return i

        #check if the player could win on their next move, and block them
        for i in range(1,10):
            copy = getboardcopy(leboard)
            if isSpaceFree(copy, i):
                makeMove(copy,playerLetter, i)
                if winner(copy, playerLetter):
                    return i

        #Try to take one of the corner, if free
        move = chooseRandomMoveFromList(leboard, ['top-L', 'top-R', 'low-L', 'low-R'])
        if move != None:
            return move

        #Try to take the center if it is free
        if isSpaceFree(leboard, 'mid-M' ):
            return 'mid-M'

        #move on one of the sides
        return chooseRandomMoveFromList(leboard, ['mid-L','mid-R','top-M','low-M'])

#Is the board full?
def isBoardFull(leboard):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
        return True

print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = playerXorO()
    turn = whofirst()
    print('The ' + turn + ' will go first.')
    gameisPlaying = True

    while gameisPlaying:
        if turn == 'player':
            #player turn
            theboard(theBoard) ##
            move = getPlayerMove(theboard)
            makeMove(theBoard, playerLetter, move)

            if winner(theBoard, playerLetter):
                theboard(theBoard) ##
                print('YOU WON!')
                gameIsPlaying = False
            else:
                if isBoardFull(theboard):
                    theboard(theBoard)
                    print('The computer wins! YOU LOSE!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        theboard(theBoard)
                        print('ITS A TIE')
                        break
                    else:
                        turn = 'player'




