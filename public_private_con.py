#Apply private, public, protected and default access modifiers to the constructor

class A:
    def __int__(self,name):
        self._name=name  # protected

class B:
    def __init__(self):
        self.__age=22    # private

class C:
    def __init__(self):
        self.address='hyderabad'  # public

obj=A('sam')
print(obj._name)
obj1=B()
print(obj1._B.__age)
obj2=C()
print(obj2.address)
