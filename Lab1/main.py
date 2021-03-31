#Main will define the game board array, call these functions, and loop until the game is over.
#It will then report which player won and ask if they want to play another game and repeat if yes.

from functions import *
from constant import *

def main():
    board = ['','','','','','','','','']
    game_progress = True
    while game_progress:
        display_instructions()
        turn = 1
        player = 0
        init_board(board)
        
        turn_progress = True
        while turn_progress:
            get_move(board, player)
            if turn > 5 and check_win(board):
                print(player_name(player) + " is the WINNER!\n")
                turn_progress = False
            elif turn == 9 and check_draw(board):
                print('DRAW\n')
                show_board(board)
                turn_progress = False
            turn += 1
            player = ~player

        if play_again() == False:
            game_progress = False
    
main()