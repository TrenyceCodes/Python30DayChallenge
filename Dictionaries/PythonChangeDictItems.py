#Change values by referencing the key name and then change its value
dict1 = {
    "name": "tom",
    "age": 30,
    "id": 2
}

dict1["name"] = "tim"
print(dict1)

#we can update the dictionary using the update method
dict1.update({"age": 25})
print(dict1)