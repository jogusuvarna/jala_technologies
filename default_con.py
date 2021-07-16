#Call the constructors(both default and argument constructors) of super class from a child Class

class A:

    def __init__(self):
        self.name = 'Sam'


class B():
    age = 22

    def __init__(self, age):
        self.age = age


class C(A, B):
    def __init__(self):
        super().__init__()
        print(self.age)
        print(self.name)


obj = C()
