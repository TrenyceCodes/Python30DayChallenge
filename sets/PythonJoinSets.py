#There are different types of ways to join sets
    # union() and update() joins all items from both sets, excluding duplicates
    # intersection() keeps the duplicates only in the sets
    # difference() keeps the items from the first set that are absent in the other
    # symmetric_difference() keeps all items excluding duplicates

# using union()
set1 = {1, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {1, 2, 3, 4, 5, 6, 7}
set3 = set1.union(set2)
print(set3)

# using | to join lists
set4 = {"apple", "orange"}
set5 = {"pear", "peach"}
set6 = set4 | set5
print(set6)

#join multiple sets together
set8 = {"apple", "orange"}
set9 = {"pear", "peach"}
set10 = {1, 2, 3, 4, 5}
#my_Set = set8 | set9 | set10
my_Set = set8.union(set9, set10)
print(my_Set)

#joining a set and tuple
my_set: set = {3, 2, 3, 4, 5}
my_tuple: tuple = (9, 10)
my_union_list = my_set.union(my_tuple)
print(my_union_list)

#update method
my_set_1 = {"a", "b", "c", "d"}
my_set_2 = {1, 2, 3, 4, 5}
my_set_1.update(my_set_2)
print(f"update: {my_set_1}")

#intersection method using intersection and &
my_set_3 = {"apple", "iphone", "phone"}
my_set_4 = {"apple", "iphone", "android"}
#my_set_5 = my_set_3.intersection(my_set_4)
my_set_5 = my_set_3 & my_set_4
print(f"intersection{my_set_5}")

#intersection_update - only keeps duplicates while changing the original set
my_set_3.intersection_update(my_set_4)
print(f"intersection update: {my_set_3}")

#difference - return a new set only containing items from 
# first set not in other set
my_set_10 = {4, 1, 3}
my_set_11 = {5, 6, 7}
#my_set_7 = my_set_3.difference(my_set_11)
# - operator only works with sets with sets, no other data types lists
my_set_7 = my_set_10 - my_set_11
print(f"difference: {my_set_7}")

# difference_update method - keeps items from the first set 
# that are not in the other set
my_set_10.difference_update(my_set_11)
print(f"difference update: {my_set_10}")

#symmetric_difference() method - keep only elements not present in both sets
#my_set_12 = my_set_10.symmetric_difference(my_set_11)
my_set_12 = my_set_10 ^ my_set_11
print(f"symmetric symmetric_difference: {my_set_11}")

#symmetric_difference_update method - keeps items that are not present in both
#sets but changes the original set
my_set_13 = my_set_10.symmetric_difference_update(my_set_11)
print(f"symmetric_difference_update: {my_set_13}")