#Write a method for increment and decrement operators(++, --)


def increament():
    print("The increament loop")
    for i in range(1,6):
        i+=1   
        print(i)

def decreament():
    print("the decreament loop")
    for i in range(2,10):
        i-=1
        print(i)

increament()
decreament()
