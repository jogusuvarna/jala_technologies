#Write a program to remove the duplicate elements and return the new array

from array import *

arr=array('i',[10,20,20,50,20,50,30])
def remove_dup(duparray):
    noduparray=[]
    for element in duparray:
        if element not in noduparray:
            noduparray.append(element)
    return noduparray

print(remove_dup(arr))

