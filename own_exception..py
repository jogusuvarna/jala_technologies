#Write a program to create your own exception

class Myownexception(Exception):

    def __init__(self,exception):
        self.exception=exception

try:
    raise Myownexception("something went wrong")
except Myownexception as e:
    print("user defined exceptionis:", e.exception)
