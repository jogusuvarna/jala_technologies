'''Create a sub class for an abstract class. Create an object in the child class for the
abstract class and access the non-abstract methods'''
from abc import ABC , abstractmethod
class Student(ABC):
    @abstractmethod
    def processor(self):   #abstract method
        pass

class Desktop(Student):

    def processor(self):
        print("it's running")

class programmer():

    def work(self,com):
        print("solving issues")
        com.processor()

obj=Desktop()
obj1=programmer()
print(obj1.work(obj))
