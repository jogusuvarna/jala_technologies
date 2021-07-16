#Create an instance for the child class in child class and call abstract methods

from abc import ABC , abstractmethod
class Student(ABC):
    @abstractmethod
    def msg(self):   #abstract method
        pass

class Student1(Student):

    def msg(self):
        print("Gud evening students")

obj=Student1()
print(obj.msg)
