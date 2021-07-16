'''Create a class with PUBLIC fields and methods.
Access the public methods and fields from any class in the same package or different
package.'''

class Student1:
    def __init__(self, m1, m2):
        self.m1 = m1  # public variable
        self.m2 = m2


class Student2(Student1):
    def info(self):
        print("the student is pass")


s = Student2(45, 58)
print(s.m1)
print(s.m2)
s.info()
