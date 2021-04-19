# Joseph Sepe CS162P Lab 3

from constant import *
from dungeon import *

def main():
    playing = True
    
    while playing:
        # Initialize game
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

        # check if board is too small for number of traps + treasure + player and exit
        if MAX_SIZE**2 < (NUM_TRAPS + NUM_TREASURES + 2):
            print("Game board is too small")
            exit()
        else:
            # draw dungeon, traps, treasures, exit, and return player location
            player_current_location = create_dungeon(dungeon, NUM_TRAPS, NUM_TREASURES, trap_locations, treasure_locations, exit_location)
            display_dungeon(dungeon)
            display_instructions()

            # haven't won or lost
            while not win and not lose:
                player_next_location = get_move(player_current_location)
            
                # check if stepped on exit
                win = check_move(player_next_location, exit_location)
                
                # check if stepped on a trap
                lose = check_move(player_next_location, trap_locations)
                
                # check if stepped on treasure
                if check_move(player_next_location, treasure_locations):
                    # Remove treasure location
                    treasure_locations.remove(list(player_next_location))
                    # Add 1 gold
                    gold += 1
                    print("+1 Gold")

                    # Got all the gold
                    if len(treasure_locations) == 0:
                        print("You collected all the gold. Make it to the exit!")
                
                # update dungeon with player's next location
                update_dungeon(dungeon, player_current_location, player_next_location)
                # reset the player's current location
                player_current_location = player_next_location
                # draw dungeon
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