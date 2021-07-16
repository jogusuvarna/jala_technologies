#Print instance variables in static methods

class Student:

    staticmethod
    def msg():
        print('hello students')

obj=Student()
Student.msg()
