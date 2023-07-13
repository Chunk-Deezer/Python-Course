mylist = ["blue", 36, False] #this is a list, multiple items stored in 1 variable
print(len(mylist)) #the length is 3
thislist = list(("True", True, 1703, False, "False")) #you can also use the list constructor instead of square brackets
print(thislist[2]) #this will print 'True' because the 1st item is index 0
print(thislist[1:4]) #this will print the 2nd until the 4th items
print(thislist[-2]) #this will print the 4th item
if True in thislist:
    print("True is in the list") #this checks if True is in the list and if it is then it will print the statement
bestlist = ["blue", "red", "yellow", "green", "purple", "grey"]
thislist[3] = "black" #this will change 'green' to 'black'
thislist[1:2] = ["pink", "maroon"] #this changes a single item (red) into two (pink and maroon)
thislist.insert(3, "orange") #this inserts orange as the 4th term without replacing anything
print(thislist) #this should now read 'blue, pink, maroon, orange, black, purple, grey'
anotherlist = ["zero", "one", "two"]
anotherlist.append("three") #the append method inserts an item at the end of a list
yetanotherlist = ["four", "five", "six"]
anotherlist.extend(yetanotherlist) #this combines the lists
print(anotherlist) #this will return the lists that have been combined
simplelist = ["porsche", "bmw", "ford"]
simplelist.pop(1) #the pop method removes the specified index and without the number removes the last item
print(simplelist)
biggestlist = ["yes", "no"]
del biggestlist[1]#this deletes the 2nd item from the list, without the brackets or number it deletes the whole list
print(biggestlist)
biggestlist.clear() #this removes the items in the list but keeps the empty list