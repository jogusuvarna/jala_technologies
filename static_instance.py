#Call instance methods in static methods

class Shape:

    def info(self):
        print('this method is used to representing the different shapes')

    staticmethod
    def show(self,msg):
       print(msg)
       print("this method identify the shapes")


Shape.show=staticmethod(Shape.info)
Shape.show("hello")
