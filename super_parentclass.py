#Call constructor of the parent class using super()

class A:
    def __init__(self):
        print("method of class A")


class B(A):
    def __init__(self):
        super().__init__()
        print("method of class B")


B()
