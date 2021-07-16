#Create an instance for the child class in child class and call non-abstract methods

from abc import ABC , abstractmethod
class Student(ABC):
    @abstractmethod
    def processor(self):   #abstract method
        pass

class Desktop(Student):
    def processor(self):
        print("it's running")


obj=Desktop()
obj.processor()
