#Booleans:
#you can evaluate any expression to get a true or false answer
print(7 < 90)
print(8 == 9)
#you can also use if statements
a=98
b=99
if a < b:
    print("b is greater than a")
else:
    print("b is not greater than a")

#you can evaluate any value with the bool() function
x="hello"
y=0
print(bool(x)) #this will be true
print(bool(y)) #this will be false
#the value 0 will return false if it is made from the __len__ function
class myclass():
    def __len__(self):
        return 0
myobj=myclass
print(bool(myobj))
#you can also check if an object is a certain data type
j=28
print(isinstance(j, int))
#in python there are basic arithmetic operators like:
print(8 + 9) #addition
print(8 * 9) #multiplication
print(8 ** 9) #powers(like 9^2)
print(9 / 3) #division
print(9 - 3) #subtraction
#and logical operators
k=1
l=3
m=1
print(bool(k < 2 and k > -5)) #this will be true
print(bool(k > 8 or k < 8 )) #this will be true
print(bool(not(k > 8 or k < 8))) #this will be false

print(bool(l is k)) #this will be false
print(bool(k is m)) #this will be true