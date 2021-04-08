# Asks user for integer, validates if in range and returns that integer
def get_num_of_names(min_val, max_val):
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
    while True:
        print("\nEnter a name:")
        choice = input()
        return choice
        
def insert_array(array, count, value):
    if count >= len(array):
        raise IndexError
    
    index = count - 1

    # move up if item is larger than value
    while index >= 0 and array[index] > value:
        array[index+1] = array[index]
        index -= 1
    
    # put in the new value and increase count
    array[index+1] = value
    count += 1
    return count

# fillArray, add Name
def fill_array(array, num_of_names):
    for i in range(num_of_names):
        insert_array(array, i, get_name())

# display only the array elements that have values
def display_array(array, count):
    print("\nList of names:")
    for i in range(count):
        print(array[i])

# Binary search, return true if value is present in the array
def bin_search(array, count, search_value):
    print("\nPerforming binary search for: " + search_value + "\n")
    min = 0
    max = count - 1
    found = False
    
    # split array in 2 and search each half
    while (max >= min and not found):
        # get mid index
        mid = (min + max) // 2
        # if mid == search , then found true
        if array[mid] == search_value:
            found = True
        # search less than mid
        elif array[mid] < search_value:
            min = mid + 1
        # search greater than mid
        else:
            max = mid - 1
    return found

