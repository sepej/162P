# Joseph Sepe CS162P Lab 2 Part A

from functions import *

def main():
    # get amount of names to add
    num_of_names = get_num_of_names(5, 20)
    # init empty array
    name_array = ['']*num_of_names

    # fill array
    fill_array(name_array, num_of_names)

    # display array
    display_array(name_array, num_of_names)

    # binary search 5 times
    for i in range(5):
        print("\nSearch")
        search_value = get_name()
        if bin_search(name_array, num_of_names, search_value):
            print(search_value + " found!")
        else:
            print(search_value + " not found :(")
    
    exit()
    
if __name__ == '__main__':
    main()