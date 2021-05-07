from person import *

class Employee:
    # init employee class composition
    def __init__(self, first_name = "", last_name = "", age = None):
        self.__person = Person(first_name, last_name, age)
    
    # return employee name
    def get_employee_name(self):
        return self.__person.get_first_name() + " " + self.__person.get_last_name()
    
    # return employee age
    def get_employee_age(self):
        return self.__person.get_age()

    