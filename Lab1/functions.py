def displayInstructions():
    # display instructions
    print('Welcome to Tic-tac-toe')
    print('')

def initBoard(board):
    getMove(board, 0)


def showBoard(board):
    for idx, value in enumerate(board):
        if value == '':
            value = str(idx+1)
        if (idx+1) % 3 == 0:
            print('[' + value + ']')
        else:
            print('[' + value + ']', end='')
    print('')

def validMoves(board):
    validMoves = []
    for idx, value in enumerate(board):
        if value == '':
            validMoves.append(idx+1)
    return validMoves

def getMove(board, player):
    # get move
    playerChar = 'X'
    if player == 0:
        print("It's X's turn\n")
    else:
        playerChar = 'O'
        print("It's O's turn\n")
    showBoard(board)

    valid = validMoves(board)
    while True:
        print("Move: ")
        choice = input()
        choiceInt = int(choice)
        if choiceInt in valid:
            board[choiceInt-1] = playerChar
            break
        else:
            print("Please choose a valid move")
            showBoard(board)
    showBoard(board)
    

    # get a move from player
        #validate the move is an integer and in range
        #verify that location is currently empty
        #update that location on the board with the player’s marker
    #does not have an explicit return, the board is updated via reference

def checkWin(board):
    1,2,3
    4,5,6
    7,8,9

    

    

#def checkDraw():
    #draw

#def playAgain():
    #playagain?

#def yesNo():
    #yes no

