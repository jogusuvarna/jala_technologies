#Call an overridden method with super class reference to B and C class’s objects

class A():
     def info(self):
         print("the information in A")

class B(A):
    pass
class C(B):
    pass

obj=B()
obj.info()

obj=C()
obj.info()

#and


class A():
     def info(self):
         print("the information in A")

class B(A):
    def info(self):
        print("the information in B")
class C(B):
    pass

obj=C()
obj.info()
obj=B()
obj.info()

