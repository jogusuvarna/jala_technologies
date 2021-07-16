'''Create a class with PRIVATE fields, private method and a main method. Print the fields
in main method. Call the private method in main method.'''

class Student1:
     def __init__(self, m1,m2):
         self.__m1=m1                # private variable
         self.__m2=m2


s=Student1(45,58)
dir(s)
print(s._Student1__m1)
print(s._Student1__m2)
