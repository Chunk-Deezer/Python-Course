#Dictionaries are ordered, changeable and do not allow duplicates
firstdict = {
    "colour": "red",
    "size": "medium", #they use curly brackets and are written in the key: value format
    "type": "fruit"   #the values can be any type
}
print(firstdict["type"])
constructdict = dict(colour = "green", shape = "cylinder", classif = "vegetable") #the dict constructor is dict()
cucumbershape = constructdict["shape"]   #you can access the items of a dictionary like this
cucumbercolour = constructdict["colour"] #or like this

cukeys = constructdict.keys() #you can get the keys for a dictionary with the keys() method
cuvalues = constructdict.values() #you can get the values in a dictionary with the values() method
print(cukeys, cuvalues)
#if you make a change in the dictionary, the lists just made get updated too
cuitems = constructdict.items() #this returns all the items in a dictionary as tuples in a list
carrot = {
    "colour": "orange",
    "size": "medium",
    "type": "vegetable",
    "age": 3
}
carrot["age"] = 4 #you can change the value of an item by referring to its key name
carrot.update({"size": "large"}) #the update() method updates a value in a dictionary but the argument must be a dictionary or iterable object with key:value pairs
carrot.pop("age") #the pop method removes the item with the specified key name
carrot["shape"] = "longcone" #you can add items in a dictionary by referring to a nonexistant key name and assigning it a value
carrot.popitem() #the popitem() method removes the last inserted item
del carrot["colour"] #the del keyword removes the item the key refers to
#the del keyword can also delete the whole dictionary if specified
print(carrot) #this should only print the size and type of carrot now
clearveg = {
    "clear": "clear",
    "this": "this",
    "dict": "dict"
}
clearveg.clear() #the clear method just clears the whole dictionary
print(clearveg)
