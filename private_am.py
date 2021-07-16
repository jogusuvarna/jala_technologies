#Create a sub class and try to access the private fields and methods from sub class.

class Student1:
     def __init__(self, m1,m2):
         self.__m1=m1                # private variable
         self.__m2=m2

class Student2(Student1):
     def info(self):
         print("student1 is pass")


s=Student2(45,50)
print(s._Student1__m1)

#Note: we can be access and modified the private variables only in class not in the outside of the class.

