#There are 6 ways to join sets
set1 = {1,2,3}
set2 = {4,5,6}
set3 = {7,8,9}
set4 = set1.union(set2) #this method creates a new set
print(set4)
set4.update(set3) #this method simply adds to an already created set
print(set4)
#both exclude duplicate items
set4.intersection_update(set1) #this metod returns a set of only the duplicate items of both sets
print(set4) 
set6 = {1,4,7}
set5 = set6.intersection(set2) #this method creates a new set of the duplicate items of both sets
print(set5)
set2.symmetric_difference_update(set5) #this method returns a set of only the items that aren't in both sets
print(set2)
set7 = set6.symmetric_difference(set3) #this method returns a new set of only the item that aren't in boths sets
print(set7)
#All of the following values should return true
megaset = {1,4,7,1,2,3}
a = set7.isdisjoint(set1)
b = megaset.issubset(set6)
c = megaset.issuperset()
print(a,b,c)