#Python Sets
#Sets are immutable, unordered, and nonIndexed, duplicates are not allowed
#Sets items appear in random order
set1 = {"hello", "hi"}
print(set1)

#Sets values True and 1 are the same and considered duplicates
# False and 0 are the same and considered duplicates just like True and 1
set2 = {True, 1, 2, 3, False, 0, 3}
print(set2)

#to get the length of a set we use the builtin function len()
print(len(set2))