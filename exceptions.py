 #Write a program to generate Arithmetic Exception without exception handling

def fun():
    x=2/0
try:
    fun()
except:
    print("we can't do zero division")
