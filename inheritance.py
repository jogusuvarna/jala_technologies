
'''A, B and C are classes

A is a super class. B is a sub class of A. C is a sub class of B.

Create three methods in each class, 2 methods are specific to each class and third
method (override method) should be in all three Classes A, B and C'''

class A():
    def fun1(self):
        print("paternt class fun1 working")

    def fun2(self):
        print("paternt class fun2 working")

    def fun3(self):
        print("paternt class fun3 working")

class B(A):
    def fun4(self):
        print("child class fun4 working")

    def fun5(self):
        print("child class fun5 working")

    def fun6(self):
        print("child class fun6 working")

class C(B):
    def fun7(self):
        print("child class fun4 working")

    def fun8(self):
        print("child class fun5 working")

    def fun9(self):
        print("child class fun6 working")


