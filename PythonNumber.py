#python numbers 
# int, float, complex
import random

x = 1 #int type positive, or negative number
y = 2.8 #float type positive, negative, containing multiple decimals
#float can also be specified in e to show the power of 10
l = 2e1

z = 1j #complex 
a = 3+5j #j represents the imaginary number, so 3 is the real number 
#while 5 is the imaginary
print(x, y, z)
print(l)
print(a)

print(float(x)) #converts variable x to a float type
print(int(y)) #converts variable y to a int type
print(complex(x)) #converts complex x to a complex type
print(complex(a)) #converts complex y to a complex type
print(random.randbytes(2))