# Joseph Sepe CS162P Lab 6A

from person import *
from employee import *

def main():
    # create empty person
    person1 = Person()
    person1.display_person()

    # create another person with input
    person2 = Person("Joseph", "Sepe", 32)
    person2.display_person()

    # test setters and getters
    person2.set_first_name("Firstname")
    person2.set_last_name("Lastname")
    person2.set_age(33)
    print(person2.get_first_name())
    print(person2.get_last_name())
    print(person2.get_age())
    person2.display_person()

    # create an employee
    employee = Employee("Joseph", "Sepe", 32)
    print(employee.get_employee_name())
    print(employee.get_employee_age())

    exit()

if __name__ == '__main__':
    main()