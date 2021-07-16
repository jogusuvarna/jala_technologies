#Write a program with finally block

a=10
b=5
try:
    print("open")
    print(a/b)
except Exception as e:
    print("the exception is",e)

finally:
    print("close")
