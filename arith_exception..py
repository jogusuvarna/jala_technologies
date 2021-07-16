#Write a program to generate Arithmetic Exception
try:
    a=2
    b=0
    print(a/b)
except ZeroDivisionError as e:
    print(e)
