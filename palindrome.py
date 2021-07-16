#Write a program to palindrome or not.

stg="jala technologies"
rev=reversed(stg)
if list(stg)==list(rev):
    print("palindrome")
else:
    print("not palindrome")
