#Create an abstract class with abstract and non-abstract methods.

'''Note: Python by default doesn’t support abstract class directly, we need to use
module abc (abstract base class).'''


from abc import ABC , abstractmethod
class computer(ABC):
    @abstractmethod
    def processor(self):   #abstract method
        pass

    def processor1(self):
        print("running")



obj=computer()    # we can not create instance for the abstract class. it shows an error

