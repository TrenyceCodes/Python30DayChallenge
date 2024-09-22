#Python Change List Items
thisList = [1, 2, 3, 4, 5, 6, 7]
thisList[1] = 4
print(thisList)

#Change a Range of Item Values
thisList[1:3] = ["hello", "world"]
print(thisList)
thisList[1:2] = ["h"] #replaces hello to h
print(thisList)

#insert items
thisList.insert(4, "i")
print(thisList)