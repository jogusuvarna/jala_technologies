#Handle the Arithmetic exception using try-catch block
a=15
b=0
try:
    print(a/b)
except Exception as e:
    print("the exception is:",e)
