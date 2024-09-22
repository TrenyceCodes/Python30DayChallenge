#Python has 4 data type lists
#Lists
#Tuple
#Set
#Dictionary 
# List is a collection which is ordered and changeable. 
    # Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. 
    # Allows duplicate members.
#Set is a collection which is unordered, 
    # unchangeable*, and unindexed. 
    # No duplicate members.
#Dictionary is a collection which is ordered** 
    # and changeable. No duplicate members.


#create a list
#list are changeable and allows duplicates
#items can be any data type, string, int, boolean
list1 = [1, 2, 3, 4]
print(list1)
list2 = ["apple", "apple", "banana"]
print(list2)
#shows number of items in list
print(len(list1))
print(len(list2))
#checks data type of list
print(type(list1))
print(type(list2))
#access items
print(list1[1])
print(list2[1])
#negative indexing
print(list1[-1]) #prints out last item
print(list2[-1]) #prints out last item
print(list1[-2]) #prints out second last item
print(list2[-2]) #prints out second last item
#index range
#shows items start at index 1(included) 
# and end at index 3(not included)
print(list1[1:3]) 
print(list2[:3])
print(list2[1:])

if "apple" in list2:
    print("Apple is in the list")