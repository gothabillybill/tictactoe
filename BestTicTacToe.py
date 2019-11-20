import random

def drawBoard(board): # DRAWS BOARD
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def getHumanLetter():
    humanletter = ''
    while (humanletter != 'X' or humanletter != 'O'):
        print('Do you want to be X or O?')
        humanletter = input()
        if humanletter.upper() == 'X':
            return ['X','O']
        elif humanletter.upper() == 'O':
            return ['O','X']

def whoGoesFirst():
    whogoesfirst = random.randint(0,1)
    if whogoesfirst == 0:
        print('You are going to move first.')
        return 'hum'
    else:
        print('The computer moves first.')
        return 'com'

def boardCopy(board): # MAKES COPY OF BOARD
    copy = []
    for i in board:
        copy.append(i)
    return copy

def makeMove(board,move,letter): # CHANGES LIST WHEN MOVE IS MADE
    board[move] = letter

def isEmpty(board, move): # RETURNS TRUE IF SPACE IS EMPTY
    if board[move] == ' ':
        return True
    else:
        return False

def isWinner(board, letter): # RETURNS TRUE IF PLAYER WON
    return ((board[1] == letter and board[2] == letter and board[3] == letter)
    or (board[4] == letter and board[5] == letter and board[6] == letter)
    or (board[7] == letter and board[8] == letter and board[9] == letter)
    or (board[1] == letter and board[4] == letter and board[7] == letter)
    or (board[2] == letter and board[5] == letter and board[8] == letter)
    or (board[3] == letter and board[6] == letter and board[9] == letter)
    or (board[1] == letter and board[5] == letter and board[9] == letter)
    or (board[3] == letter and board[5] == letter and board[7] == letter))


def humanMove(board, letter):
    move = 0
    while str(move) not in ['1 2 3 4 5 6 7 8 9'.split()] or isEmpty(board, move) is False:
        move = int(input('Type your move: '))
        return move

def gameOver(board):
    if ' ' not in board:
        return True
    else:
        return False

def chooseRandomMove(board, movelist):
    return random.choice(movelist)

#############################################################################
def comMove(board, comletter):
    if humanletter == 'X':
        comletter = 'O'
    else:
        comletter = 'X'
    for move in range(1,10):
        if isEmpty(board, move):
            boardcopy = boardCopy(board)
            testmove = makeMove(boardcopy, move, comletter)
            if isWinner(boardcopy, comletter):
                return move
    for move in range (1,10):
        if isEmpty(board, move):
            boardcopy = boardCopy(board)
            makeMove(boardcopy, move, humanletter)
            if isWinner(boardcopy, humanletter):
                return move
            corners = [1, 3, 7, 9]
            while corners != []:
                move = chooseRandomMove(board, corners)
                if isEmpty(board, move):
                    return move
                else:
                    corners.remove(move)
            if corners == [] and isEmpty(board, 5):
                return move
            sides = [2, 4, 6, 8]
            while sides != []:
                move = chooseRandomMove(board, sides)
                if isEmpty(board, move):
                    return move
                else:
                    sides.remove(move)

#############################################################################

print('Welcome to Tic Tac Toe\n')

humanletter, comletter = getHumanLetter()

board = [' '] * 10

turn = whoGoesFirst()

gameisplaying = True
while gameisplaying:
    move = 0
    while turn == 'hum':
        move = humanMove(board, humanletter)
        makeMove(board, move, humanletter)
        if isWinner(board, humanletter):
            drawBoard(board)
            print('You won!')
            gameisplaying = False
            break
        else:
            turn = 'com'
    while turn == 'com':
        move = comMove(board, comletter)
        makeMove(board, move, comletter)
        if isWinner(board, comletter):
            drawBoard(board)
            print('The computer won!')
            gameisplaying = False
            break
        elif gameOver(board) is True:
            gameisplaying = False
        else:
            drawBoard(board)
            turn = 'hum'

print('Game Over.')