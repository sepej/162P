from hashlib import new
from constant import *
import random

def create_dungeon(dungeon, num_traps, num_treasures, trap_locations, treasure_locations, exit_location):
    spaces_taken = []
    player_location = []
    # randomly place traps
    i = 0
    while i < num_traps:
        random_row = random.randint(0,MAX_SIZE-1)
        random_col = random.randint(0,MAX_SIZE-1)
        if [random_row, random_col] not in spaces_taken:
            dungeon[random_row][random_col] = 'T'
            spaces_taken += [[random_row, random_col]]
            trap_locations += [[random_row, random_col]]
            i += 1
    # randomly place treasures
    i = 0
    while i < num_treasures:
        random_row = random.randint(0,MAX_SIZE-1)
        random_col = random.randint(0,MAX_SIZE-1)
        if [random_row, random_col] not in spaces_taken:
            dungeon[random_row][random_col] = 'G'
            spaces_taken += [[random_row, random_col]]
            treasure_locations += [[random_row, random_col]]
            i += 1         
    #randomly place player
    while player_location == []:
        random_player_row = random.randint(0,MAX_SIZE-1)
        random_player_col = random.randint(0,MAX_SIZE-1)
        if [random_player_row, random_player_col] not in spaces_taken:
            dungeon[random_player_row][random_player_col] = 'P'
            spaces_taken += [[random_player_row, random_player_col]]
            player_location = random_player_row, random_player_col
    #randomly place exit
    while exit_location == []:
        random_exit_row = random.randint(0,MAX_SIZE-1)
        random_exit_col = random.randint(0,MAX_SIZE-1)
        if [random_exit_row, random_exit_col] not in spaces_taken:
            dungeon[random_exit_row][random_exit_col] = 'E'
            spaces_taken += [[random_exit_row, random_exit_col]]
            exit_location += [random_exit_row, random_exit_col]
    
    #return player starting location as a tuple
    return player_location

def display_dungeon(dungeon):
    #print dungeon
    for row in range(MAX_ROW):
        for col in range(MAX_COL):
            print(dungeon[row][col], end=" ")
        print("")


def get_move(player_location):

    legal_move = False
    while legal_move == False:

        #get move from from user and validate
        print("Move your character with W, A, S, or D")
        player_move = get_and_check_valid_move_input()

        if player_move == 'w':
            player_location = player_location[0]-1, player_location[1]
        elif player_move == 'a':
            player_location = player_location[0], player_location[1]-1
        elif player_move == 's':
            player_location = player_location[0]+1, player_location[1]
        elif player_move == 'd':
            player_location = player_location[0], player_location[1]+1
        
        if (player_location[0] not in range(0, MAX_ROW)) or (player_location[1] not in range(0, MAX_COL)):
            print("Out of bounds. Not a legal move")
            legal_move = False
        else: #valid location inside dungeon
            legal_move = True
    #return new player location as tuple
    return player_location

# Passes in the move and then returns w,a,s,d
def get_and_check_valid_move_input():
    valid = ['w', 'a', 's', 'd']
    answer = None
    while answer == None:
        choice = input()
        choice = choice.lower()
        if choice in valid:
            answer = choice
        else:
            print("Please type W, A, S, or D")
    return answer

def check_move(player_next_location, type_of_object_locations):
    player_move = list(player_next_location)
    move = None
    if player_move in list(type_of_object_locations) or player_move == list(type_of_object_locations):
        move = True
    else:
        move = False
    return move

def update_dungeon(dungeon, player_current_location, player_next_location):
    current_row, current_col = player_current_location
    next_row, next_col = player_next_location
    dungeon[next_row][next_col] = PLAYER
    dungeon[current_row][current_col] = SPACE


# Play again question
def play_again():
    return yes_no("Do you want to play again? (y/n)")

# Passes in the question and then returns true or false for yes or no
def yes_no(question):
    valid = ['y', 'n']
    answer = None
    while answer == None:
        print(question)
        choice = input()
        choice = choice.lower()
        if choice in valid:
            if choice == 'y':
                answer = True
            else:
                answer = False
        else:
            print("Please type y or n")
    return answer