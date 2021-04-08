from functions import *

def main():
    num_of_names = get_num_of_names(5, 20)
    name_array = ['']*num_of_names

    fill_array(name_array, num_of_names)

    display_array(name_array, num_of_names)

    for i in range(6):
        print("\nSearch")
        search_value = get_name()
        if bin_search(name_array, num_of_names, search_value):
            print(search_value + " found!")
        else:
            print(search_value + " not found :(")
    
    exit()
    
if __name__ == '__main__':
    main()