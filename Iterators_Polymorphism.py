#An iterator is an object that contains a countable number of values, and can be iterated on
#iterated on = traverse through all the values
mystring = "Hello"
myit = iter(mystring) #the iter() method gets an iterator from an iterable object
for x in range(len(mystring)):
    print(next(myit)) 
#examples of iterable objects are all the arrays and strings

