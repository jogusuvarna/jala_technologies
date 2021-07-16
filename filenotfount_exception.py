#Write a program to generate FileNotFoundException

try:
    with open("doc.txt") as file:
        read_doc=file.read()

except FileNotFoundError as e:
    print("generated:",e)


