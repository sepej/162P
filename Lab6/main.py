# Joseph Sepe CS162P Lab 6B

from helper import *

def main():
    employees = []
    # get number of employees to enter
    print("How many employees work at the company?")
    num_employees = get_integer(1, 10)
    
    # create an employee and add it to the list for num_employees
    for i in range(num_employees):
        new_employee = create_employee()
        employees.append(new_employee)

    display_employees(employees)

    exit()

if __name__ == '__main__':
    main()