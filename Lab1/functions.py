def display_instructions():
    # display instructions
    print('\nWelcome to Tic-Tac-Toe\nTry to get 3 in a row!')

def init_board(board):
    for idx, value in enumerate(board):
        board[idx] = ''

def player_name(player):
    if player == 0:
        return 'X'
    else:
        return 'O'

def show_board(board):
    for idx, value in enumerate(board):
        if value == '':
            value = str(idx+1)
        if (idx+1) % 3 == 0:
            print('[' + value + ']')
        else:
            print('[' + value + ']', end='')
    print('')

def valid_moves(board):
    validMoves = []
    for idx, value in enumerate(board):
        if value == '':
            validMoves.append(idx+1)
    return validMoves

def get_move(board, player):
    # get move
    if player == 0:
        player_char = 'X'
        print("\nIt's X's turn\n")
    else:
        player_char = 'O'
        print("\nIt's O's turn\n")
    show_board(board)

    valid = valid_moves(board)
    while True:
        print("Move: ")
        choice = input()
        choice_int = int(choice)
        if choice_int in valid:
            board[choice_int-1] = player_char
            break
        else:
            print("Please choose a valid move")
            show_board(board)

def check_win(board):
    if board[4] == board[0] and board[4] != '':
        if board[4] == board[8]:
            board[0] = '\\'
            board[4] = '\\'
            board[8] = '\\'
            show_board(board)
            return True
    if board[4] == board[2] and board[4] != '':
        if board[4] == board[6]:
            board[2] = '/'
            board[4] = '/'
            board[6] = '/'
            show_board(board)
            return True
    if board[4] == board[1] and board[4] != '':
        if board[4] == board[7]:
            board[1] = '|'
            board[4] = '|'
            board[7] = '|'
            show_board(board)
            return True
    if board[0] == board[3] and board[0] != '':
        if board[0] == board[6]:
            board[0] = '|'
            board[3] = '|'
            board[6] = '|'
            show_board(board)
            return True
    if board[8] == board[5] and board[8] != '':
        if board[8] == board[2]:
            board[2] = '|'
            board[5] = '|'
            board[8] = '|'
            show_board(board)
            return True
    if board[8] == board[7] and board[8] != '':
        if board[8] == board[6]:
            board[6] = '-'
            board[7] = '-'
            board[8] = '-'
            show_board(board)
            return True
    if board[4] == board[3] and board[4] != '':
        if board[4] == board[5]:
            board[3] = '-'
            board[4] = '-'
            board[5] = '-'
            show_board(board)
            return True
    if board[0] == board[1] and board[0] != '':
        if board[0] == board[2]:
            board[0] = '-'
            board[1] = '-'
            board[2] = '-'
            show_board(board)
            return True
    return False

def check_draw(board):
    if check_win(board) == False:
        return True

def play_again():
    return yes_no("Do you want to play again? (y/n)")

def yes_no(question):
    valid = ['y', 'n']
    while True:
        print(question)
        choice = input()
        choice = choice.lower()
        if choice in valid:
            if choice == 'y':
                return True
            else:
                return False
        else:
            print("Please type y or n")