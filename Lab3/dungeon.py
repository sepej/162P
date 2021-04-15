import constant
import random

def create_dungeon(dungeon, num_traps, num_treasures):
    """
    #randomly place traps and treasures
    #randomly place player and exit
    #make sure each item is place in separate location
    #return player starting location as a tuple
    """

def display_dungeon(dungeon):
    """
    #print dungeon
    #no return values
    """

def get_move(player_location):
    """
    #get move from from user and validate
    
        #legal move
        #valid location inside dungeon
    #return new player location as tuple
    """

def check_move(dungeon, player_next_location, type_of_object):
    """
    #check the move to see if onto a space containing an object of the type being checked
    #returns true if the move is onto such a space
    #return false if not
    """

def update_dungeon(dungeon, player_previous_location, player_next_location):
    """
    #place a new player marker and clear the old spot
    #nothing is returned
    """

def play_again():
    """
    #return true if player wants to play again, false otherwise
    """