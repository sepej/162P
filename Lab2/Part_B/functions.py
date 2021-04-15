# Asks user for integer, validates if in range and returns that integer
def get_integer(min_val, max_val):
    integer = None
    while (integer not in range(min_val, max_val+1)):
        print("Enter a number between " + str(min_val) + " and " + str(max_val))
        integer = input()
        try:
            integer = int(integer)
        except ValueError:
            print("Not a number.")
    return integer

# get a name, check if not an empty string
def get_name():
    name = ""
    name_valid = False
    while (name_valid == False):
        print("\nEnter a name:")
        name = input()
        if name != "":
            name_valid = True
        else:
            print("Please enter a name.")
    return name

# get an L number, check if not an empty string
def get_lnum():
    lnum = ""
    lnum_valid = False
    while (lnum_valid == False):
        print("\nEnter a Lnumber:")
        lnum = input()
        if lnum != "":
            lnum_valid = True
        else:
            print("Please enter a Lnumber.")
    return "L00" + lnum

# insert values, sort by Lnumber on insert
def insert_lists(lnum_array, name_array, count, lnum, name):
    if count >= len(lnum_array) or count >= len(name_array):
        raise IndexError
    
    # get index
    index = count - 1

    # move up if item is larger than value, keep lists parallel
    while index >= 0 and lnum_array[index] > lnum:
        lnum_array[index+1] = lnum_array[index]
        name_array[index+1] = name_array[index]
        index -= 1

    # put in the new values
    lnum_array[index+1] = lnum
    name_array[index+1] = name

# selection sort, sort by name
def sort_lists_by_name(name_array, lnum_array, count):
    # Sorting by name (value)
    #loop for each
    for i in range(count):
        min_index = i
        for j in range(i+1, count):
            # compare name values
            if name_array[j] < name_array[min_index]:
                min_index = j
        # swap values, do each array to keep parallel
        name_array[i], name_array[min_index] = name_array[min_index], name_array[i]
        lnum_array[i], lnum_array[min_index] = lnum_array[min_index], lnum_array[i]

# fill lists, add name and Lnumber
def fill_lists(name_array, lnum_array, num_students):
    for i in range(num_students):
        name = get_name()
        lnum = get_lnum()
        insert_lists(lnum_array, name_array, i, lnum, name)

# display only the array elements that have values
def display_array(count, array, array_2=None):
    for i in range(count):
        if array_2 != None:
            print(array[i] + ", " + array_2[i])
        else:
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