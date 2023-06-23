#Number types:
x=8908 #This is data type int
y=8.908 #this is data type float
z=8908j #This is data type complex
#you can change data types from one to another
a=float(x) #Changes to float
b=int(z) #Changes to int
#c=complex(y) #This will not work, you cannot change a number to complex type
print(type(a))
print(type(b))

import random #This is a random function that is built in

print(random.randrange(1, 10))