# Display instructions
def display_instructions():
    print('\nWelcome to Tic-Tac-Toe\nTry to get 3 in a row!')

# Reset board, rewrites the board list with ''
def init_board(board):
    for idx, value in enumerate(board):
        board[idx] = ''

# Get the player name, Returns X or O
# Adds the possibility of letting players type their own names in.
def player_name(player):
    if player == 0:
        return 'X'
    else:
        return 'O'

def player_char(player):
    if player == 0:
        return 'X'
    else:
        return 'O'

# Display the board
def show_board(board):
    for idx, value in enumerate(board):
        if value == '':
            value = str(idx+1)
        if (idx+1) % 3 == 0:
            print('[' + value + ']')
        else:
            print('[' + value + ']', end='')
    print('')

# Returns the valid move
def valid_moves(board):
    validMoves = []
    for idx, value in enumerate(board):
        if value == '':
            validMoves.append(idx+1)
    return validMoves

# Enter the player's move
def get_move(board, player):
    # Print player's name, calling function
    print("\nIt's " + player_name(player) + "'s turn\n")

    show_board(board)

    # Get a list of valid moves for the current board
    valid = valid_moves(board)
    # Enter the players move into the list
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

# Check win condition, returns true or false
def check_win(board):
    # Check two squares, if they are the same then check the next in the sequence
    if board[4] == board[0] and board[4] != '':
        if board[4] == board[8]:
            # Player won, change the array to display a line where they won.
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

# Check draw, if no win's then return true
def check_draw(board):
    if check_win(board) == False:
        return True

# Play again question
def play_again():
    return yes_no("Do you want to play again? (y/n)")

# Passes in the question and then returns true or false for yes or no
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