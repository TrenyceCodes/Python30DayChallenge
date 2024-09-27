#Dictionaries
# stores a key:value pairs
# doesn't allow duplicates
# ordered list
# mutable

#create a dictionary
dict1 = {
    "name": "Tom",
    "Dob": "11/08/2005",
    "age": "30"
}

print(dict1["name"])  #prints dictionary item attached to key `name`

#print dictionary length
print(len(dict1))

#dictionaries can hold any data type
dict2: dict = {
    "brand": "Ford",
    "electric": False,
    "year": 2009,
    "colors": ["red", "white", "green", "yellow"],
}

print(dict2["colors"])

#use the builtin function type to check for dictionary type which is `dict`
print(type(dict2))

#use the dict constructor to make a dictionary without using the curly brackets
dict3: dict = dict(id=1, name="foo")
print(dict3["id"])
