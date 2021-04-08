from functions import *
from globals import *

def main():

    num_of_names = get_integer(5, 20)
    name_array = ['']*20

    fill_array(name_array, num_of_names)

    display_array(name_array)

    for i in range(6):
        search_value = get_name()
        if bin_search(name_array, search_value):
            print(search_value + " found!")
        else:
            print(search_value + " not found :(")
    
    exit()
    
main()