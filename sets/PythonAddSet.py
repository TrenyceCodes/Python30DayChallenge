#To add a item to a set, we use to built in function add()
set1 = {"berry", "peach", 1}
set1.add("orange")
print(set1)

#update with another set to set1
set2 = {3, 5, 6, 7, 8}
set1.update(set2)
print(set1)

#add any other items from another iterable object(tuples, list, dictionaries)
myList: list = [1, 3, 4]
set1.update(myList)
print(set1)