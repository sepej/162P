#Main will define the game board array, call these functions, and loop until the game is over.
#It will then report which player won and ask if they want to play another game and repeat if yes.

from functions import *

def main():
    # Define blank board and start game progress loop
    board = ['','','','','','','','','']
    game_progress = True
    while game_progress:
        # Display instructions and set defaults
        display_instructions()
        turn = 1
        player = 0
        init_board(board)
        
        # Start turn loop
        turn_progress = True
        while turn_progress:
            # Call get move function for player
            get_move(board, player)
            # Only check win condition if turn greater than 5
            if turn > 5 and check_win(board):
                # Print the winner, end the turn loop
                print(player_name(player) + " is the WINNER!\n")
                turn_progress = False
            # If turn is 9 and nobody wins draw
            elif turn == 9 and check_draw(board):
                print('DRAW\n')
                show_board(board)
                turn_progress = False
            # Increase turn count and flip player bit.
            turn += 1
            player = ~player

        # Check if user want's to play again
        if play_again() == False:
            # If so end game progress loop.
            game_progress = False
    
main()