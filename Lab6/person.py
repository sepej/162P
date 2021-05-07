class Person:
    # initialize
    def __init__(self, first_name = "", last_name = "", age = None):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
    
    # getters
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name

    def get_age(self):
        return self.__age

    # setters
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_age(self, age):
        self.__age = age

    # display person method
    def display_person(self):
        print("Name: " + self.__first_name + " " + self.__last_name + ", Age: " + str(self.__age))