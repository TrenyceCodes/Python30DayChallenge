#we can copy dicts using copy() method so they don't need to be referenced
thisDict = {
    "name": "Tom",
    "age": 29,
    "school": "GraduateSchool"
}

myDict = thisDict.copy()
print(myDict)

#we can even use the dict() function to copy a dictionary to a new variable
myNewDict = dict(myDict)
print(myNewDict)