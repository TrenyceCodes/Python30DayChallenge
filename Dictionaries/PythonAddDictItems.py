#we can add items simply by adding a new index key and assigning a value
dict1 = {
    "species": "human",
    "eating_type": "omnivore", 
}

dict1["gender"] = ["male", "female", "other"]
print(dict1)

#we can use the update method, adding a new value too if not already 
# in dictionary
dict1.update({"origin": "pangea"})
print(dict1)