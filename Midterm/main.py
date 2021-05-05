# Joseph Sepe Midterm CS162P Spring Question 23
import random

def main():
    # new empty list with 20 values
    new_list = ['']*20

    # add a random int for each value
    for i in range(len(new_list)):
        # single digit for a better showList output 0-9
        new_list[i] = random.randint(0,9)

    sortList(new_list)
    showList(new_list)

def sortList(the_list):
    # sort using the built in sort function
    the_list.sort()
    
def showList(the_list):
    # loop for each index of the list
    for i in range(len(the_list)):
        # if position mod 5 then make a new row
        if (i+1) % 5 == 0:
            print(the_list[i])
        else:
            print(the_list[i], end=" ")

if __name__ == "__main__":
    main()