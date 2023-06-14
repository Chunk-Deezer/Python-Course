#This is an example of some variables:
x=8
y="hello"
print(x) #This line will output variable x, but not y

#This is called unpacking:
ingredients=["cake" , "butter" , "sausage"]
a,b,c=ingredients #This means the variables a,b and c take the values of the words in the list
#Here i will output the ingredients, all in one line of code
print(a,b,c)

#Now i will use global and local variables in one example here
link="blunder" #This is a global variable, outside any functions

def myfunc():
    link="mistake" #This is a local variable, inside the function
    print(link) #This will print the local variable 'link'

myfunc()

print(link) #This will print the global variable 'link'