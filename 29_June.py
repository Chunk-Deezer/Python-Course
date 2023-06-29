#you can slice strings which means printing only a section of it.
x="BananaPineapple"
print(x[:5]) #this will only print what is before line 5
print(x[5:]) #this will only print what is after line 5
#you can slice using negative indexes
print(x[-7:-1]) #this will print from the 'n' in pineapple to the 2nd 'e' in pineapple

print(x.upper()) #this will return the string in all upper case
print(x.lower()) #you can do it for lower case as well
y=" hello,all "
print(x.strip()) #this will strip the string of all whitespaces
print(x.replace("B", "P")) #this will replace the B in banana with a P
print(x.split(",")) #this will seperate the string into 2 seperate ones. it will be seperated by the ','
#you can add strings together by doing this
a="Big"
b="Mangoes"
c=a + " " + b
print(c)
#you can combine numbers and strings by using the format method
item=78
quant=9
cost=9.99
order="i want {} of the number {} which costs {}"
print(order.format(quant, item, cost))
#a backslash can let illegal characters exist in a string
txt="my dog\'s name is \"Norden\""
print(txt) #this will print the variable 'txt' with the illegal characters included