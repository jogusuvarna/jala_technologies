'''Runtime Polymorphism with Data Members/Instance variables, Repeat the above
process only for data members.'''

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1=self.m1+other.m1
        m2 = self.m2 + other.m2
        s=Student(m1,m2)
        return s


student1=Student(55,85)
student2=Student(85,85)

s=student1+student2
print(s.m1)
print(s.m2)

