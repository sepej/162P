class Student:
    # initialize
    def __init__(self, name = "", grade = 0):
        self.__name = name
        self.__grade = grade

    # getter and setter for name
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.name = name

    # getter and setter for grade
    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.grade = grade

    # display the student
    def display_student(self):
        print('Student: ' + self.get_name() + '\nGrade: ' + str(self.get_grade()))