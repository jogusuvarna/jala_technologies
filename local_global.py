# Define the local and Global variables with the same name and print both variables and understand the scope of the variables


a=10                    #global
def fun():
    a=30                #local
    print('the local variable',a)

print('the global variable',a)

fun()

