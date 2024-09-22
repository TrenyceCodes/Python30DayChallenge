#Exercises: Level 1
#Write a python comment saying 'Day 2: 30 Days of python programming'
#Day 2: 30 Days of python programming

#Declare a first name variable and assign a value to it
import math


first_name = "lauryn"
#Declare a last name variable and assign a value to it\
last_name = "holly"
#Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name
#Declare a country variable and assign a value to it
country = "USA"
#Declare a city variable and assign a value to it
city = "New York City"
#Declare an age variable and assign a value to it
age = 19
#Declare a year variable and assign a value to it
year = 2024
#Declare a variable is_married and assign a value to it
is_married = False
#Declare a variable is_true and assign a value to it
is_true = True
#Declare a variable is_light_on and assign a value to it
is_light_on = False
#Declare multiple variable on one line
l, y, z = 1, 2, 3

#Exercises: Level 2
#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type((l, y, z)))

#Using the len() built-in function, find the length of your first name
print(f"length of first name: {len(first_name)}")

#Compare the length of your first name and your last name
print(f"comparison between first and last name: {len(first_name) < len(last_name)}")

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(f"total sum: {total}")
#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(f"difference: {diff}")
#Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(f"product: {product}")
#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(f"divide: {division}")
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two
print(f"remainder: {remainder}")
#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one**num_two
print(f"exponentation: {exp}")
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one//num_two
print(f"floor_division of number one and number two: {floor_division}")

#The radius of a circle is 30 meters.
radius = 30.0
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = math.pi*radius**2
print(f"Area of a circle: {area_of_circle}")
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*math.pi*radius
print(f"Circumference of a circle: {circum_of_circle}")
#Take radius as user input and calculate the area.
radius = float(input("Enter in radius: "))
areaOfCircle = math.pi*radius**2
print(f"Area of Circle: {areaOfCircle}")
#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
firstName = input("First Name: ")
first_name = first_name
lastName = input("Last Name: ")
last_name = lastName
countryInput = input("Country: ")
country = countryInput
ageInput = input("Age: ")
age = ageInput
#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('help')