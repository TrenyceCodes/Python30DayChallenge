#Exercise: Level 2
#Check the python version you are using
from math import sqrt


print()

#Open the python interactive shell and do the following operations. The operands are 3 and 4.
#addition(+)
print(3+4)
#subtraction(-)
print(3-4)
#multiplication(*)
print(3*4)
#modulus(%)
print(3%4)
#division(/)
print(3/4)
#exponential(**)
print(3**4)
#floor division operator(//)
print(3//4)

#Write strings on the python interactive shell. The strings are the following:
#Your name
print("Trenyce")
#Your family name
print("price")
#Your country
print("USA")
#I am enjoying 30 days of python
print("I am enjoying 30 days of python")

#Check the data types of the following data:
#10
print(type(10))
#9.8
print(type(9.8))
#3.14
print(type(3.14))
#4 - 4j
print(type(4-4j))
#['Asabeneh', 'Python', 'Finland']
print(type(['Asabeneh', 'Python', 'Finland']))
#Your name
print(type("Trenyce"))
#Your family name
print(type("Price"))
#Your country
print(type("USA"))

#Exercise: Level 3
#Write an example for different Python data types 
#such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
#Number Integer
print(10)
#Number Float
print(3.14)
#Number Complex
print(3-5.2j)
#String 
print("Trenyce Price")
#Boolean
print(True)
#List 
print([True, False, 1, 2])
#Tuple
print(tuple((1, 2)))
#Set
print(set((5,4)))
#Dictionary
dictionary1 = {1: "one", 2: "two"}
print(dictionary1)

#Find an Euclidian distance between (2, 3) and (10, 8)
#x1 = 2
#x2 = 3
#y1 = 10
#y2 = 8
x1, x2, y1, y2 = 2, 3, 10, 8
distance = sqrt(((y1-x1)**2)+((y2-x2)**2))
print(distance)