# get an integer between min and max and validate
from employee import *
import csv

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
def get_a_name():
    name = ""
    name_valid = False
    while (name_valid == False):
        print("Enter a name:")
        name = input()
        if name != "":
            name_valid = True
        else:
            print("Please enter a name.")
    return name

# get a name and age and create employee
def create_employee():
    new_employee = None
    print("(First Name)")
    employee_first_name = get_a_name()
    print("(Last name)")
    employee_last_name = get_a_name()
    print("(Age)")
    employee_age = get_integer(5, 90)
    employee_job_class = get_job_class()
    if employee_job_class == "janitor":
        new_employee = Janitor(employee_first_name, employee_last_name, employee_age)
    elif employee_job_class == "cashier":
        new_employee = Cashier(employee_first_name, employee_last_name, employee_age)
    elif employee_job_class == "stocker":
        new_employee = Stocker(employee_first_name, employee_last_name, employee_age)
    print("")
    return new_employee

# return job class from user
def get_job_class():
    job_class = ["janitor", "cashier", "stocker"]
    job_valid = False
    class_input = ""
    while (job_valid == False):
        print("\nEnter a job class (janitor, cashier, stocker):")
        class_input = input().lower()
        if class_input in job_class:
            job_valid = True
        else:
            print("Please enter a job class.")
    return class_input

# get a name and age and create employee
def display_employees(employees):
    for employee in employees:
        print(employee.get_employee_name() + " aged " + str(employee.get_employee_age()) + " working as a " + employee.get_job_name() + " is a " + employee.get_job_description())
    
    # open or create the file
    with open('employees.csv', mode='w', newline='') as employees_file:
        writer = csv.writer(employees_file)
        writer.writerow(["Name", "Age", "Job", "Job Description"])
        for employee in employees:
            writer.writerow([employee.get_employee_name(),employee.get_employee_age(),employee.get_job_name(),employee.get_job_description()])
        
        # close the file
        employees_file.close()