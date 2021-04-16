import constant
import random

def create_dungeon(dungeon, num_traps, num_treasures):
    """
    #randomly place traps and treasures
    #randomly place player and exit
    #make sure each item is place in separate location

    #return player starting location as a tuple
    return player_location
    """

def display_dungeon(dungeon):
    """
    #print dungeon
    print(dungeon)
    #no return values
    """

def get_move(player_location):
    """
    #get move from from user and validate
    player_move = input()

    if legal move:
        #legal move
        #valid location inside dungeon
        #set new player location

    #return new player location as tuple
    """

def check_move(dungeon, player_next_location, type_of_object):
    """
    object_bool = None
    #check the move to see if onto a space containing an object of the type being checked
    if player_next_location == type_of_object:
        #returns true if the move is onto such a space
        object_bool = True
    else:
        #return false if not
        object_bool = False
    return object_bool
    """

def update_dungeon(dungeon, player_previous_location, player_next_location):
    """
    #place a new player marker and clear the old spot
    #nothing is returned
    """

def play_again():
    """
    #return true if player wants to play again, false otherwise
    playagain_bool = None
    play_again = input()
    if play_again true:
        playagain_bool = True
    else:
        playagain_bool = False
    return playagain_bool

    """