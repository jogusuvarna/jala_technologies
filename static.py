#Write a class with 2 static variables, 2 Instance variables, 2 static methods, 2 instance methods and a main method.

class Student:
    def __init__(self, name, age):
        self.name=name             #instance variable
        self.marks=age

    def msg(self):               # instance method
        print("hello", self.name)

    def reply(self):               # instance method
        print("hello", self.name)

    staticmethod
    def get_age(age):
        if age>17:
            print("Not belongs to school")
        else:
            print("Not belongs to school")

s1=Student('nisha', 500)
s1.msg()
Student.get_age(16)

s2=Student('nihan', 700)
s2.msg()
Student.get_age(18)
