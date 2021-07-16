#Print the fields/instance members of the parent class using super
class A:
    def __init__(self):
        self.name='sam'
        self.age=22


class B(A):
    def __init__(self):
        super().__init__()
        print('fields of parent class name', self.name)
        print('fields of parent class name', self.age)

obj=B()

