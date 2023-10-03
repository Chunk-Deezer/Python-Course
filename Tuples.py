example = ("metal", "wood", "stone", "metal") #this is a tuple, like a list but they are ordered and unchangeable and use round brackets
#there can be duplicate values and are indexed. they are also ordered and that order cant be changed
print(len(example))
tupleT = ("brown",) #this is a tuple
tupleF = ("brown")  #this is not. the comma makes the difference when working with 1 item tuples
print(type(tupleT))
print(type(tupleF))
datatuple = ("7", False, 78, 9.8, 3j) #tuples can have many different types of data stored within them
#tuple() can also be used to cast a tuple
longtuple = ("hammer", "drill", True, 333, "spanner", 99j, "crane", 16)
print(longtuple[-4:]) #range specifications work the same as lists do, this will start at 'spanner' and go until the end of the tuple
if 333 in longtuple:
    print("yes, 333 is in the tuple.")
#you cannot change a tuple, but you can change it into a list so it can be changed, then change it back.
tooples = ("two", 2)
lizscht = list(tooples)
lizscht.append("threee")
lizscht[1] = "twoo" 
tooples = tuple(lizscht) 
#you can also add a tuple to another tuple, that is allowed
tupleI = ("jam", "bread")
tupleL = ("peanut_butter",)
tupleI = tupleI =+ tupleL
#you also cannot remove items in a tuple
#but you can use the same workaround from before
finaltuple = ("sky", "ground", "sea")
print(finaltuple)
finalist = list(finaltuple)
finalist = finalist.remove("sky")
finaltuple = tuple(finalist) #this has removed the item 'sky' from the tuple
#however you can delete a tuple entirely without having to change it to a list 
del finaltuple
