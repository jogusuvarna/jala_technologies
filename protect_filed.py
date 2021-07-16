'''Create a class with PROTECTED fields and methods. Access these fields and methods
from any other class in the same package.'''

class Student1:
     def __init__(self, m1,m2):
         self._m1=m1                # protected variable
         self._m2=m2


s=Student1(45,50)
print(s._m1)
print(s._m2)

#Also, Access the PROTECTED fields and methods from child class located in a different Package

class Student1:
     def __init__(self, m1,m2):
         self._m1=m1                # protected variable
         self._m2=m2

class Student2(Student1,):
     def info(self):
         print("student1 is pass")


s=Student2(45,50)
print(s._m1)
print(s._m2)


#Access the PROTECTED fields and methods from any class in different package

class Student1:
     def __init__(self, m1,m2):
         self._m1=m1                # protected variable
         self._m2=m2

class Student2(Student1,):
     def info(self):
         print("student1 is pass")


s=Student1(45,50)
print(s._m1)
print(s._m2)
