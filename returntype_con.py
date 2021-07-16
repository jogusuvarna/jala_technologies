#Write constructors with return type int and String

class A:
    x=10
    y='20'
    def __int__(self,x):
        self.x =x
        return self.x


    def __int__(self,y):
        self.y =x
        return +str(self.x)
obj=A()
print(obj.x)
print(type(obj.x))
print(obj.y)
print(type(obj.y))
