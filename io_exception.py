#Write a program to generate IOException

try:
    f=open("test.txt","r")
    f.write("this is the content of the file")
except IOError:
    print("the error occur at finding the file")
