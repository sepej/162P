# Joseph Sepe CS162P Lab 3

from constant import *
from dungeon import *

def main():
    print("Start game")
    playing = True
    
    while playing:
        dungeon = []
        for index in range(MAX_SIZE):
            dungeon.append([SPACE] * MAX_COL)
        player_current_location = -1, -1
        player_next_location = -1, -1
        win = lose = False
        gold = 0
        trap_locations = []
        treasure_locations = []
        exit_location = []

        if MAX_SIZE**2 < (NUM_TRAPS + NUM_TREASURES + 2):
            print("Game board is too small")
            exit()
        else:
            player_current_location = create_dungeon(dungeon, NUM_TRAPS, NUM_TREASURES, trap_locations, treasure_locations, exit_location)
            display_dungeon(dungeon)
            #display_instructions()
            while not win and not lose:
                player_next_location = get_move(player_current_location)
            
                # check if stepped on exit
                win = check_move(player_next_location, exit_location)
                #print(check_move(player_next_location, exit_location))
                
                if not win:
                    # check if stepped on a trapd
                    if check_move(player_next_location, trap_locations):
                        lose = True
                
                if not win and not lose:
                    # check if stepped on treasure
                    if check_move(player_next_location, treasure_locations):
                        #TODO Remove treasure location
                        gold += 1
                        print("+1 Gold")
                    
                    update_dungeon(dungeon, player_current_location, player_next_location)
                    player_current_location = player_next_location
                    display_dungeon(dungeon)
                
            # Report if won or lost
            if lose:
                print("You stepped on a trap and died.")
            if win:
                print("You made it out alive with " + str(gold) + " gold.")
            # Ask to play again
            playing = play_again()
    exit()

if __name__ == "__main__":
    main()