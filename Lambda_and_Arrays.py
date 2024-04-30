example = lambda a,b : a +  b + 10 #a lambda is a small anonymous function 
print(example(10,7)) #lambdas can take any number of arguments

def lambfunc(c):
    return lambda n : n * c #lambdas are normally used in a function, the function defintion taking one argument and one being unknown
mydoubler = lambfunc(2)
mytripler = lambfunc(3) #this is using the function definition to create a function that triples the number sent in
print(mydoubler(10))    #to define n you have to put an argument in the brackets
print(mytripler(11))

#Arrays beyond this point

cars = ["BMW", "Ford", "Volkswagen"]
cars[-1] = "Volvo" #you can refer to a specific point in an array by using square brackets with the index, after the variable name
length = len(cars) #the len() method gives you the length of the array (number of items stored within)
print("you have these cars: ", cars, "and there are ", length, " of them")

numbers = ["one", "two", "three", "four", "five"]
numbers.append("six") #you can use the append method to add an item on the end of an array
for x in numbers: #you can use a for loop to loop through the list items and print them
    print(x)
    numbers.pop(0) #the pop method removes the specified element in the array

sentence = ["i", "did", "not", "eat", "my", "food"]
sentence.remove("not") #you can also use the remove method but you have to refer to the element value, not the index