# Joseph Sepe CS162P Lab 2 Part B

from functions import *

def main():
    # init empty arrays
    name_array = ['']*20
    lnum_array = ['']*20

    # get amount of names and Lnumbers to add
    num_students_to_insert = get_integer(5, 20)

    # fill array, sorting by lnumber on insert
    fill_lists(name_array, lnum_array, num_students_to_insert)
    
    print("\nBefore selection sort:")
    display_array(num_students_to_insert, name_array, lnum_array)
    
    # bubble sort lists by name
    sort_lists_by_name(name_array, lnum_array, num_students_to_insert)

    print("\nAfter selection sort:")
    display_array(num_students_to_insert, name_array, lnum_array)

    # binary search 5 times
    for i in range(5):
        print("\nSearch")
        search_value = get_name()
        if bin_search(name_array, lnum_array, num_students_to_insert, search_value):
            print(search_value + " found!")
        else:
            print(search_value + " not found :(")
    
    exit()
    
if __name__ == '__main__':
    main()