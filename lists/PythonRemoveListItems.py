#Python - Remove List Items'
list1 = list()
list1.append("hello")
list1.append("world")
first_item, *rest = list1
print(rest)

#Remove Specified Item
thisList = ["apple", "banana", "orange"]
thisList.remove("apple")
print(thisList)

thisList.append("apple")
thisList.remove("apple")
print(thisList)