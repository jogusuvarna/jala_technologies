''' Write two methods with the same name but different number of parameters of different
data type and call the methods from main method'''

class Operationd:
    def __init__(self):
        print("overloading with same function")

    def sum(self, a,b,f=None):
        s = c + d +f
        return s

    def sum(self,c='hello',d='world'):
        e=c+d
        return e

obj=Operationd()
print(obj.sum(14,15))
print(obj.sum())
