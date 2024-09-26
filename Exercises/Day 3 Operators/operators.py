# Exercise Day 3
import math
#Declare your age as integer variable
age = 19
#Declare your height as a float variable
height = 5.2
#Declare a variable that store a complex number
money = 20 + 3j
#Write a script that prompts the user to enter base and height of the triangle
# and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter base: "))
height = int(input("Enter height: "))
print(f"The area of the triangle is {base * height}")
#Write a script that prompts the user to enter side a, side b, and side c of the triangle.
# Calculate the perimeter of the triangle (perimeter = a + b + c).
sideA = int(input("Enter side a: "))
sideB = int(input("Enter side b: "))
sideC = int(input("Enter side c: "))
print(f"The perimeter of the triangle is {sideA + sideB + sideC}")
#Get length and width of a rectangle using prompt.
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))
print(f"the area of the rectangle is {length * width}")
print(f"the perimeter of the rectangle is {2*(length+width)}")
#Get radius of a circle using prompt.
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input("Enter radius of circle: "))
pi = math.pi
area = pi * radius**2
circumference = 2 * pi * radius
print(f"The area of the circle {area}")
print(f"The circumference of the circle {circumference}")
#Calculate the slope, x-intercept and y-intercept of y = 2x -2

#Slope is (m = y2-y1/x2-x1).
# Find the slope and Euclidean distance between point (2, 2) and point (6,10)

#Compare the slopes in tasks 8 and 9.

#Calculate the value of y (y = x^2 + 6x + 9).
# Try to use different x values and figure out at what x value y is going to be 0.

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
lenOfPython = len("python")
lenOfDragon = len("dragon")
print([True if lenOfDragon > lenOfPython else False])

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
if "on" in "python" and "dragon":
    print("On is found in both string")

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
if "jargon" in "I hope this course is not full of jargon.":
    print("Jargon is found in string")

#There is no 'on' in both dragon and python
if "on" in "python" and "dragon":
    print(True)
else:
    print(False)

#Find the length of the text python and convert the value to float and convert it to string
pythonLength = len("python")
print(str(float(pythonLength)))

#Even numbers are divisible by 2 and the remainder is zero.
# How do you check if a number is even or not using python?
number = 10
if number % 2 == 0:
    print(f"{number} is divisible by 2 and even")
else:
    print(f"{number} is not divisible by 2 and odd")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))

#Check if type of '10' is equal to type of 10
print(type("10") == type(10))

#Check if int('9.8') is equal to 10
print(int(9.8) == 10)

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
print(f"Your weekly earning is {hours * rate_per_hour}")

#Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
seconds = 31536000
print(f"You have lived for {years * seconds} seconds.")

#Write a Python script that displays the following table