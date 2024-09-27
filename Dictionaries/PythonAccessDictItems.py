#Accessing items using brackets []
dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

dict1Object = dict1["brand"]

#get the value of a model key using the get method
dict1BrandKey: dict[str, str] = dict1.get("brand")
print(dict1BrandKey)

#get a list of keys
dict1Keys: dict[str, any] = dict1.keys()
print(dict1Keys)

#get a list of values from dictionary
dict1Values: dict[str, any] = dict1.values()
print(dict1Values)

#get items of dictionary in a key:item pair
dict1Items: dict[str, any] = dict1.items()
print(dict1Items)

#check if a key exists in the dictionary
if "brand" in dict1:
    print("brand is in dictionary 1")

for key, value in dict1.items():
    print(f"key:value pair -> {key}:{value}")