#Write a program to find the prime or not.

n=int(input("enter the number:"))
if n>1:
  for i in range(2,n):
      if (n%i)==0:
          print(n, "is the prime number")
          print(i, "times", n // i, "is", n)
          break
      else:
        print(n,"is not the prime number")
