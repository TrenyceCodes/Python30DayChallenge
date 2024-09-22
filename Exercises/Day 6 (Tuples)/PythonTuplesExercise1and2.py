#Exercises: Level 1
#Create an empty tuple
tuple1 = tuple()
print(tuple1)

#Create a tuple containing names of your sisters and your brothers 
brothers = tuple(("christian", "tj"))
print(brothers)

sisters = tuple(("lauryn", "diamond"))
print(sisters)

# (imaginary siblings are fine)

#Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

#How many siblings do you have?
print(len(siblings))

#Modify the siblings tuple and 
# add the name of your father and mother 
# and assign it to family_members
siblingsList = list(siblings)
siblingsList.append("Mom")
siblingsList.append("Dad")
family_members = tuple(siblingsList)
print(family_members)

# Exercise 2
#Unpack siblings and parents from family_members
brothersItem, sisters, *parents = family_members
print(brothersItem, sisters, *parents)

#Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits_products = ("apple", "orange", "cantaloupe")
vegetables_products  = ("tomato", "lettuce", "carrot")
animal_products  = ("sheep", "cow", "chicken")
food_stuff_tp = fruits_products + vegetables_products + animal_products
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_list = list(food_stuff_tp)

#Slice out the middle item or items from the food_stuff_tp tuple 
# or food_stuff_lt list.
middleItems = food_stuff_list[3:5]
print(middleItems)

#Slice out the first three items 
#and the last three items from food_staff_lt list
firstThreeProducts = food_stuff_list[:3]
print(f"first three products of food stuff list: {firstThreeProducts}")
lastThreeProducts = food_stuff_list[-3:]
print(f"last three products of food stuff list: {lastThreeProducts}")

#Delete the food_stuff_tp tuple completely
del food_stuff_tp
#print(f"delete the food_stuff_tp tuple completely {food_stuff_tp}") 

#Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#   Check if 'Estonia' is a nordic country
e = 0
for e in range(len(nordic_countries)): 
    if nordic_countries[e] == "Estonia":
        print(f"Estonia is found at index {e}")
    else:
        print(f"Estonia is not found")
        break

#   Check if 'Iceland' is a nordic country
i = 0
for i in range(len(nordic_countries)):
    if nordic_countries[i] == "Iceland":
        print(f"Iceland is found at index {i}")
        i = i + 1