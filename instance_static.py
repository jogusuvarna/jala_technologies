#Call static methods in instance methods

class Shape:

    def info(self):
        print('this method is used to representing the different shapes')
    staticmethod
    def show(msg):
        print(msg)
        print("this method identify the shapes")


Shape.show=staticmethod(Shape.show)
Shape.info=Shape.show('hello')
