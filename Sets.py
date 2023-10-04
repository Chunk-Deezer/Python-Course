#sets are unordered, unchangeable and unindexed. they also do not allow duplicate values
#they are written with curly brackets
firstset = {"which", "order", "will", "it", "be"} #you do not know what order the set items will appear in, they are unordered
print(firstset)

duplicateset = {"good", "bad", "good", "bad", "bad"} #duplicate items will be ignored
print(duplicateset)
#the values True and 1 are considered the same
#the construtor for a set is set()
castset = set(("apple", "berry", "banana")) #double round brackets needed

#you can't access items in a set by referring to an index, but you can loop through them using a for
for x in castset:
    print(x)
#you can also ask if a specified value is in the set by using in
print("banana" in castset)

setchanging = {"basketball", "football", "tennis"}
setchanging.add("rugby") #you can us the add() method to add an item to the set
print(setchanging)

setupdate = {"pool", "chess", "swimming"}
setchanging.update(setupdate) #the update() method adds items from 1 set to another
print(setchanging)
#the object in the update() method can be any iterable object like a list or tuple

#to remove items from a set, you can use remove() or discard()
#the only difference is that if the item to remove is not there, remove() will raise an error, discard() will not
setremoving = {"floor", "ceiling", "window"}
setremoving.remove("ceiling")
setremoving.discard("wall") #both of these will raise no error

poppingset = {1, 2, 3, 4, 5}
y = poppingset.pop() #the pop() method removes a random item, and the return value is the popped item
print(y)

#the clear() method removes all items from the set
#del will delete the set as a whole
deletedset = {"goodbye", "cruel", "world"}
deletedset.clear()
print(deletedset) #this will not raise an error, it still exists but just with no value

del deletedset
#print(deletedset) #this would raise an error because it no longer exists