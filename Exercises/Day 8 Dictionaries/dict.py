#1. create an empty dictionary called dog
dog = {}

#2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = "Sunny"
dog["color"] = "Black and tan"
dog["breed"] = "German Shepherd"
dog["legs"] = 4
dog["age"] = 10

#Create a student dictionary and 
# add first_name, last_name, gender, age, marital status, 
# skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Beatriz",
    "last_name": "Hall",
    "gender": "Female",
    "age": 21,
    "marital_status": "single",
    "skills": ["writing", "reading"],
    "country": "United States",
    "city": "New York City",
    "address": "123 west main street"
}

#4. Get the length of the student dictionary
print(f"the length of the student dictionary is: {len(student)} \n")

#5. Get the value of skills and check the data type, it should be a list
print(f"the value of skills and data type is: skills->{(student["skills"])}, type: -> {type(student["skills"])} \n")

#6. Modify the skills values by adding one or two skills
student["skills"].append("skiing")
student["skills"].append("karate")
print(f"Updated student skills: {student["skills"]} \n")

#7. Get the dictionary keys as a list
dictKeys = []
for k in student.keys():
    dictKeys.append(k)
print(dictKeys)
#or
dictKeys = list(student.keys())
print(f"Dictionary keys: {dictKeys} \n")

#8. Get the dictionary values as a list
dictValues = []
for v in student.values():
    dictValues.append(v)
print(dictValues)
#or
dictValues = list(student.values())
print(f"Dictionary values: {dictValues} \n")

#9. Change the dictionary to a list of tuples using items() method
dict_tuple = tuple(list(student.items()))
print(f"Dictionary tuple: {dict_tuple} \n")

#10. Delete one of the items in the dictionary
del student["age"]

#11. Delete one of the dictionaries
del dog