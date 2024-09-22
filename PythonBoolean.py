a = 500
b = 300

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

#evaluate values and variables
print(bool("Hello"))
print(bool(17))
#prints out false
print(bool("")) #prints false
print(bool(0)) #prints false
print(bool(False)) 
print(bool(None))
print(bool([])) #print false
print(bool(()))
print(bool({}))

#prints out false
class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

#returns true from function myFunction
def myFunction():
    return True

print(myFunction())

if myFunction():
    print("YES!")
else:
    print("NO!")

x = 200
#checks variable type(True or False)
print(isinstance(x, int)) 