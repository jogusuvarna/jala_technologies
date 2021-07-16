'''Write two methods with the same name but different number of parameters of same type
and call the methods from main method'''


class Operation:
    def __init__(self):
        print("overloading with same function")

    def sum(self, a, b, f=None):
        s = c + d
        return s

    def sum(self,c=14,d=64):
        e=c+d
        return e

obj=Operation()
print(obj.sum(14,15))
print(obj.sum())
