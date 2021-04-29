from student import *

# get an integer between min and max and validate
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
def get_student_name():
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

# get a name and grade and create and return a Student
def create_student():
    student_name = get_student_name()
    student_grade = get_integer(1, 12)
    new_student = Student(student_name, student_grade)
    return new_student 

# selection sort, sort list of student objects by name
def sort_students_by_name(students):
    #loop for each
    count = len(students)
    for i in range(count):
        min_index = i
        for j in range(i+1, count):
            # compare name values
            if students[j].get_name() < students[min_index].get_name():
                min_index = j
        # swap object locations in list
        students[i], students[min_index] = students[min_index], students[i]
