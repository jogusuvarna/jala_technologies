#Call static methods and instance methods in main method`

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def info(self):
        print("hello")

    staticmethod
    def test():
        print("test the programme")

obj=Student(55,45)
obj.info()
Student.test=staticmethod(Student.test)
obj.test()
