#Write two methods with the same name, number of parameters and data type but different return Type.
class Operationd:
    def __init__(self):
        print("overloading with same function")

    def sum(self, a,b):
        s = a+b
        return s

    def sum(self,c='good ',d='morning'):
        e=c+d
        return e

obj=Operationd()
print(obj.sum(14,15))
print(type(obj.sum(14,15)))
print(obj.sum())
print(type(obj.sum()))

