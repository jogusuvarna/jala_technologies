#Write two methods with the same name and same number of parameters of different type and call from main method

class Operationd:
    def __init__(self):
        print("overloading with same function")

    def sum(self, a,b):
        s = a + b
        return s

    def sum(self,c='good ',d='mornig'):
        e=c+d
        return e

obj=Operationd()
print(obj.sum(14,15))
print(obj.sum())
