#Python Tuples
#unchangeable
#ordered
#allows duplicates
#Tuple is one of 4 built-in data types in Python 
# used to store collections of data,
# String, int and boolean data types: 
# the other 3 are List, Set, and Dictionary, 
# all with different qualities and usage.

#create a tuple
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(tuple1))
print(len(tuple1))

#duplicate tuple
tuple2 = (1, 2, 3, 4, 5, 6, 7, 7)
for index, value in enumerate(tuple2):
    print(f'{index} -> {value}')

#create a tuple with one item
tuple3 = ("apple",)
print(type(tuple3))
#not a tuple
tuple4 = ("apple")

#tuple constructor
tuple5 = tuple(("apple","hello"))
print(type(tuple5))