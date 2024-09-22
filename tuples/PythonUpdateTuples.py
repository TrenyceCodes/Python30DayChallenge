#Python Update Tuples
#Change Tuple Values
tupleX = ("apple", "banana", "orange")
tupleY = list(tupleX)
tupleY[1] = "kiwi"
tupleX = tuple(tupleY)
print(tupleX)

#add items
thisTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
listTuple = list(thisTuple)
listTuple.append("orange")
thisTuple = tuple(listTuple)
print(thisTuple)
#second option
y = ("apple",)
thisTuple += y
print(thisTuple)

#Remove items
tuple2 = (True, False, False)
o = list(tuple2)
o.remove(True)
tuple2 = tuple(o)
print(tuple2)
del tuple2