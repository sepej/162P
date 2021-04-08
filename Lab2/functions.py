from globals import *

# Asks user for integer, validates and returns that integer
def get_integer(min_val, max_val):
    # Add validation
    while True:
        print("Enter a number between " + str(min_val) + " and " + str(max_val))
        choice = input()
        try:
            choice = int(choice)
            if choice in range(min_val, max_val+1):
                return choice
            else:
                print("Not valid. Try again")
        except ValueError:
            print("Not a number.")

def get_name():
    # Add validation
    while True:
        print("\nEnter a name:")
        choice = input()
        return choice
        
def insert_array(array, count, value):
    if count >= len(array):
        raise IndexError
    
    index = count - 1

    while index >= 0 and array[index] > value:
        array[index+1] = array[index]
        index -= 1
    
    array[index+1] = value
    count += 1
    return count


# fillArray, add Name
def fill_array(array, num_of_names):
    global count
    for i in range(num_of_names):
        count = insert_array(array, count, get_name())

def display_array(array):
    global count
    print("\nList of names:")
    for i in range(count):
        print(array[i])

# Binary search, return true if value is present in the array
def bin_search(array, search_value):
    global count
    print("\nPerforming binary search for: " + search_value + "\n")
    min = 0
    max = count - 1
    found = False
    
    while (max >= min and not found):
        mid = (min + max) // 2
        if array[mid] == search_value:
            found = True
        elif array[mid] < search_value:
            min = mid + 1
        else:
            max = mid - 1
    return found

