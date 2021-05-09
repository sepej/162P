from person import Person

# get the definitions of Abstract Base Class
# and abstract method to use in defining Employee
from abc import ABC, abstractmethod

class Employee(ABC):
    # init employee class composition
    def __init__(self, first_name = "", last_name = "", age = None):
        self.__person = Person(first_name, last_name, age)
    
    # return employee name
    def get_employee_name(self):
        return self.__person.get_first_name() + " " + self.__person.get_last_name()
    
    # return employee age
    def get_employee_age(self):
        return self.__person.get_age()
    
    # abstract method
    @abstractmethod
    def get_job_name(self):
        pass

    # abstract method
    @abstractmethod
    def get_job_description(self):
        pass

class Janitor(Employee):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def get_job_name(self):
        return "Janitor"
    def get_job_description(self):
        return "Sanitation Engineer"

class Cashier(Employee):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def get_job_name(self):
        return "Cashier"
    def get_job_description(self):
        return "Customer Service Specialist"

class Stocker(Employee):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def get_job_name(self):
        return "Stocker"
    def get_job_description(self):
        return "Merchandise Distribution Associate"

    