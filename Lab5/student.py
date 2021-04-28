#displayStudent
#o used to create the output to display single student
#o no input
#o returns a string that indicates the student’s name and what grade they are in


class Student:
    def __init__(self, name = "", grade = 0):
        self.__name = name
        self.__grade = grade

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.name = name

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.grade = grade

    def display_student(self):
        print('Student: ' + self.get_name() + '\nGrade: ' + str(self.get_grade()))