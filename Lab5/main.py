from student import *
from helper import *

def main():
    # define empty student list
    students = []

    # get number of students to enter
    print("How many students do you want to enter?")
    num_students = get_integer(1, 20)
    
    # create a student and add it to the list for num_students
    for i in range(num_students):
        new_student = create_student()
        students.append(new_student)

    # selection sort students by name
    sort_students_by_name(students)

    # display all students
    for x in students:
        x.display_student()

    exit()

if __name__ == '__main__':
    main()