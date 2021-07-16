#Try to call the constructor multiple times with the same object(*)
class A:
    def __int__(self):
        self.x = 10


obj = A()
obj = A()
print(obj)
print(obj)
