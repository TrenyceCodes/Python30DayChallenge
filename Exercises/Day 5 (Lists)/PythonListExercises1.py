#Exercises: Level 1
#Declare an empty list
list1 = list()
list2 = []

#Declare a list with more than 5 items
fruits = ["apples", "bananas", "peaches", "cantaloupe", "pear"]

#Find the length of your list
len(fruits)

#Get the first item, 
# the middle item and the last item of the list
fruits[0]
fruits[2]
fruits[len(fruits)-1]

#Declare a list called mixed_data_types, 
# put your(name, age, height, marital status, address)
mixed_data_types = ["Trenyce", "18", "5'2", "single", "416"]

#Declare a list variable named it_companies 
# and assign initial values Facebook, Google, 
# Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#Print the list using print()
print(it_companies)
#Print the number of companies in the list
print(len(it_companies))
#Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[len(it_companies)-1])
#Print the list after modifying one of the companies
it_companies[1] = "Youtube"
print(it_companies)
#Add an IT company to it_companies
it_companies.append("Meta")
print(it_companies)
#Insert an IT company in the middle of the companies list
it_companies.insert(3, "Wipro")
#Change one of the it_companies names to uppercase (IBM excluded!)
for it in it_companies:
    if it == "Facebook":
        print(it.upper())

print(it_companies)

#Join the it_companies with a string '#;  '
companies = "#".join(it_companies)
print(companies)

#Check if a certain company exists in the it_companies list.
if "Apple" in it_companies:
    print("Apple is already in the list")

#Sort the list using sort() method
for i in range(0, len(it_companies)):
    for j in range(i+1, len(it_companies)):
        if it_companies[i] >= it_companies[j]:
            it_companies[i], it_companies[j] = it_companies[j], it_companies[i]
print(it_companies)
it_companies.sort()

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
it_companies[::-1]
print(it_companies)

#Slice out the first 3 companies from the list
x_out = slice(3)
print(it_companies[x_out])

#Slice out the last 3 companies from the list
['Youtube', 'Wipro', 'Oracle', 
 'Microsoft', 'Meta', 'IBM', 
 'Facebook', 'Apple', 'Amazon']
x = slice(6, 9)
print(f"last three companies {it_companies[x]}")

#Slice out the middle IT company or companies from the list
y = slice(4,5)
print(f"the middle it company {it_companies[y]}")

#Remove the first IT company from the list
it_companies.remove("Youtube")
del it_companies[0]
print(it_companies)

#Remove the middle IT company or companies from the list
it_companies.remove("Meta")
del it_companies[2:3] #removes meta
print(it_companies)

#Remove the last IT company from the list
it_companies.remove("Amazon")
del it_companies[len(it_companies)-1]
print(it_companies)

#Remove all IT companies from the list
del it_companies
#print(it_companies) #successfully deleted llist

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
full_stack = front_end.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)