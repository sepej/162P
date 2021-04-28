from student import *
from helper import *

def main():
    students = []
    print("How many students do you want to enter? (1-20)")
    num_students = get_integer(1, 20)
    
    for i in range(num_students):
        new_student = create_student()
        students.append(new_student)

    sort_students_by_name(students)
    for x in students:
        x.display_student()

if __name__ == '__main__':
    main()