#Number types:
x=8908 #This is data type int
y=8.908 #this is data type float
z=8908j #This is data type complex
#you can change data types from one to another, this is called casting
a=float(x) #Changes to float
b=int(y) #Changes to int
#c=complex(y) #This will not work, you cannot change a number to complex type
print(type(a))
print(type(b))

import random #This is a random function that is built in

print(random.randrange(1, 10))

f="joules"
print(f[3]) #this will print the 4th character (character 1 is counted as line 0)