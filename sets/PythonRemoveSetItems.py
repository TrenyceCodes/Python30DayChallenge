#To remove an item from a set we can use 
#   remove(), discard(), pop(), del method, clear(), 
set1 = {1, 2, 3, 4, 5}

#remove method, returns an error
set1.remove(1)
print(set1)

#discard method, doesnt return an error
set1.discard(2)
print(set1)

#pop method, removes random item and returns that pop item
poppedItem = set1.pop()
print(poppedItem)
print(set1)

#clear method, empties set and returns clear set list
set1.clear()
print(set1)

#del method, deletes set, returning an error if called after deletion
del set1
print(set1)