#Python Strings
#Strings are arrays of bytes representing unicode characters

#Quotes inside Quotes
print("It's alright")
print("Hello, Tom")

#assign string to variable
a = "Hello"
print(a)

#multiline string three double or single quotes
z = """
Lorem ipsum odor amet, consectetuer adipiscing elit. 
Magnis placerat ac tellus aptent maximus integer ut adipiscing consequat. 
Libero cubilia fermentum, ultricies tortor gravida cras.
"""
print(z)

#access element in string array
b = "Hello, world"
print(b[2:5])
print(b[1])
print(len(b)) #string length
print(b[2:5]) #slicing string, starting from index 2 to 5 
#(not including before 2 and after 5)

#slicing from start
print(b[:5]) #ends at position 5(not including position 5)
#slicing to the end
print(b[2:]) #starts at position 2 and continues on
#negative indexing
print(b[-3:]) #works backwards from the array(right to left) 

#loop through string array
for x in "banana":
    print(x)

#check if certain character or phrase is in string array
txt = "the best things in life are free!"
print("free" in txt) #prints out boolean value true or false
print("expensive" not in txt) 

if "free" in txt:
    print("Yes 'free' is present.")

if "expensive" not in txt:
    print("No 'expensive' is present")