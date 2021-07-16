'''Write a class with a default constructor, one argument constructor and two argument
constructors. Instantiate the class to call all the constructors of that class from a main
class'''

class A:
    def __init__(self,name):                # one argument constructor
        self.name=name
class B():
    num1=0
    num2 = 0
    sum=0
    def __init__(self,num1,num2):             # two  argument constructor
        self.num1 = num1
        self.num2 = num2

    def Addition(self):
        self.sum=self.num1+self.num2

    def display(self):
        print("enter the num1:", (self.num1))
        print("enter the num1:", (self.num2))
        print("sum of numbers:", (self.sum))

    def __int__(self):                                   #default constructor
        self.addition="adding the the numbers"

obj1=A('Satya')
print(obj1.name)
obj=B(20,30)
obj.Addition()
obj.display()
