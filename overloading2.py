#Write two methods with the same name and same number of parameters of same type and call from main method

class Operationd:
    def __init__(self):
        print("overloading with same function")

    def sum(self, c,d):
        s = c + d
        return s

    def sum(self,a=100,b=50):
        e=a + b
        return e

obj=Operationd()
print(obj.sum(14,15))
print(obj.sum())
