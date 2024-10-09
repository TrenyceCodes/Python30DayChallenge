#Python Conditions and If Statements
# Equals: a == b
# Not Equals: a != b
# Less Than: a < b
# Less Than or Equal to: a <= b
# Greater Than: a >= b
# Greater Than or Equal to: a >= b

#We can create an if statement using the if keyword
# we can also use elif statements too with elif and else keywords
import random


a = 335
b = 337
if b > a:
    print(f"{b} is greater than {a} \n")
elif a > b:
    print(f"{a} is greater than {b} \n")
elif a == b:
    print(f"{a} and {b} are equal to each other \n")
else:
    print("error \n")

#short hand if  (ternary operators or conditional expressions)
if a > b: print(f"{a} is greater than {b} \n")

#short hand if else
print(f"{a} is greater than {b} \n") if a > b else print(f"{b} is greater than {a} \n")

#we can also use multiple else statements on the same line
print(f"{a} is greater than {b} \n") if a > b else print(f"{a} and {b} are equal to each other \n") if a == b else print(f"{b} is greater than {a} \n")

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")

    if n % 2 == 0 and range(2, 6):
        print("Not Weird")

    if n % 2 == 0 and range(6, 21):
        print("Weird")

    if n % 2 == 0 and n > 20:
        print("Not Weird")