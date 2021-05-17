class Person:
    # initialize
    def __init__(self, first_name = "", last_name = "", age = 0):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
    
    # getters
    def getFirstName(self):
        return self.__first_name
    
    def getLastName(self):
        return self.__last_name

    def getAge(self):
        return self.__age

    # setters
    def setFirstName(self, first_name):
        self.__first_name = first_name

    def setLastName(self, last_name):
        self.__last_name = last_name

    def setAge(self, age):
        self.__age = age

    # display person method
    def displayPerson(self):
        print("Name: " + self.__first_name + " " + self.__last_name + ", Age: " + str(self.__age))