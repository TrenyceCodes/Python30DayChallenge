#Unpacking tuple
fruits = ("pear", "apple", "orange")
red, pink, blue = fruits
print(f"{red}, {pink}, {blue}")

#using asterisk
(purple, *rest) = fruits
print(f"{purple}, {rest}")