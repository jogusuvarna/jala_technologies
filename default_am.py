''' Create a class with DEFAULT fields and methods. Access these fields and methods
from any other class in the same package.'''

class Student1:
     def __init__(self):
         self.name='sam'
         self.marks=75


s=Student1()
print(s.name)
print(s.marks)
