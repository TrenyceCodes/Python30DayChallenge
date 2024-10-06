#we can do a nested dictionary like this or
myShoppingCart: dict[str, dict[str, float]] = {
    "item1" : {
        "name": "sock",
        "cost": 3.75
    },
    "item2" : {
        "name": "t-shirt",
        "cost": 2.59
    },
    "item3" : {
        "name": "Vans Men's old skool",
        "cost": 48.05
    }
}

#like this 
item1: dict[str, float] = {
    "name": "sock",
    "cost": 3.75
}
item2: dict[str, float] = {
    "name": "t-shirt",
    "cost": 2.59
}
item3: dict[str, float] = {
    "name": "Vans Men's old skool",
    "cost": 48.05
}

myShoppingCart1: dict[str, dict[str, float]] = {
    "item1": item1,
    "item2": item2,
    "item3": item3
}

#to access an item in nested dictionaries 
# we can use names from the outer dictionaries
print(myShoppingCart1["item1"]["name"]) #prints item1 name

#to loop through nested dictionaries we can use the items() method
for index, item in myShoppingCart1.items():
    print(f"index and items: {index, item} \n")

    for i in item:
        print(f"items: {i + ':', item[i]} \n") 