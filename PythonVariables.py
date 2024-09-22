# Python variables
#python variables
x = 5
y = "Hello world" #this is variable y with the string value of hello world
y = 4 #variable y is now changed to value int 4
print(y)

#casting - can specify or change data type of variable
print(str(x))
print(int(y))
print(float(x))

#type - gets the data type of variable
print(type(x)) 
print(type(y))

#assign multiple values, to different variables
l, m, n = "hello", "world", "today"
print(l)
print(m)
print(n)

#assign one value to multiple variables
a = b = c = "banana"
print(a)
print(b)
print(c)

#unpack a collection
cars = ["honda", "ford", "mustang"]
x, y, z = cars
print(x)
print(y)
print(z)
print(x, y, z)
print(x + y + z)

#global variables - can be used inside and outside the functions
def printVariable():
    global y
    y = "purple"

printVariable()
print("my favorite color is " + y)