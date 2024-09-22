#Python Add List Items
thisList = ["Mangosteen", "Boysenberry", "Acai", "Corn Kernel"]
thisList.append("Jambul") #adds it to the end of the list
print(thisList)

#Insert items by index(added as new item, doesn't replace current item)
thisList.insert(3, "Soursop")
print(thisList)

#Extend List - adds lists to current list
candies = ["Gushers", "Bubble Tape", "Salt Water Taffy", "Pop Rocks"] 
thisList.extend(candies) #adds candies to end of thisList lists elements
print(thisList)

#add any iterable(tuples, sets, dictionaries)
#An iterator is an object that contains a countable number of values.
#An iterator is an object that can be iterated upon, 
# meaning that you can traverse through all the values.
thisOrchids = ("Restrepia", "Phragmipedium")
thisList.extend(thisOrchids)
print(thisList)