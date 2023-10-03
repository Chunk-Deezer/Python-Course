firsttuple = ("no", "maybe", "yes") #this is called packing a tuple

(answer1, answer2, answer3) = firsttuple #this is called unpacking a tuple
print(answer1)
print(answer2)
print(answer3)

verylongtuple = ("orange", "mango", "pineapple", "papaya", "apple", "kiwi")
(orange, *tropical, multicoloured, hairy) = verylongtuple #if the number of variables is less than the number of values then you can 
#use an asterisk, which assigns multiple values to one variable as a list. if the asterisk is added to a variable name that isnt the 
#last, it will assign values until the number of variable names and values are equal
packedtuple = ("yellow", "green", "white", "purple")
for x in packedtuple:
    print(x) #you can loop through items in a tuple using a for loop

for i in range(len(packedtuple)):
    print(packedtuple[i]) #using the range and len functions you can create a suitable iterable, and loop through the tuple by 
    #referring to the index number

while i < len(packedtuple):
    print(packedtuple[i]) #you can use while loop to loop through the tuple, by comparing variable i to the length of the tuple
    i = i + 1 #this means that you create a suitable iterable (i)

tuple1 = (1, 10, 100)
tuple2 = ("one", "ten", "100")
tuple3 = tuple1 + tuple2 #you can also join tuples with the + operator

tupleMulti = tuple2 * 3 #you can also multiply the content of a tuple with the * operator

#tuple methods:
print(tuple2.count("one")) #this returns the number of times a specific value occurred in the tuple
print(tuple1.index(100))   #this searches for the given value and returns the position where it was found