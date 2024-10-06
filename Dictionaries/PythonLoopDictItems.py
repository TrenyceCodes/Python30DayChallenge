dict1 = {
    "name": "tom",
    "age": 30,
    "id": 2
}

#prints key names from dict 1 one by one
for x in dict1:
    print(dict1[x])

#print all values in dictionary using values() method
for x in dict1.values():
    print(f"print items using values() method: {x}")

#we can also use keys() method to return the keys of the dictionary
for i in dict1.keys():
    print(f"print keys from dict1 using keys() method: {i}")

#we can loop through the whole dictionary using items() method
for x, y in dict1.items():
    print(f"key: {x} <--> value: {y}")