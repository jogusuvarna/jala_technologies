'''
Create a class with main method. Create an object for each class A, B and C in main
method and call every method of each class using its own object/instance.'''

class A():
     def __init__(self):
         print("class A constructer")

class B(A):
    def __init__(self):
        print("class B constructer")

class C(B):
    def __init__(self):
        print("class C constructer")

obj=A()
obj1=B()
obj3=C()
