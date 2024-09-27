#There are different ways to remove items from the dictionary
dict1: dict[str, str] = {
    "scientific_name": "Lavandula",
    "Family": "Lamiaceae",
    "Subfamily": "Nepetoideae",
    "Genus": "Lavandula; L.",
    "Kingdom": "Plantae"
}

# we can use the pop method
dict1.pop("Family")
print(dict1)

#we can also use the popitem method to remove the last inserted item
dict1.popitem()
print(dict1)

#we can also use the del keyword to delete a certain item and 
#delete the whole dictionary
del dict1["Genus"]
#del dict1
print(dict1)

# we can use the clear method to empty the dictionary
dict1.clear()
print(dict1)