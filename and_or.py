#Programs on Logical AND,OR operator and Logical NOT

a=30
b=20
c=40
if a>b and a>c:
    print("a is greater than both b and c")
else:
    print("a is greater than either b or c")

if a>10 or b>10:
    print("either number of greater than 10")
else:
    print("no number grater than 10")


a=10
if not(a%4==0 or a%6==0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")

