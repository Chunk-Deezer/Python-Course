def examplefunc(colour):       #a function is created with the def keyword
    print(colour + " apples") #on the line above, the word inside the brackets (colour), is called an parameter which is used
examplefunc("green")           #this is called an argument, used to pass data into a function           #to pass data into a function

#the number of arguments must match the number of parameters or an error will be raised
def arbitraryfunc(*colours): #this is an arbitrary argument, you add a * before the parameter name if the number of arguments that
    print("my favourite type of apples are the "+ colours[-1]+ " ones") #are going to be passed through the function is unknown
arbitraryfunc("blue", "red", "green", "yellow") #the fucntion will recieve a tuple of arguments and accesses them accordingly

def keywordfunc(kid1, kid2, kid3):
    print("the youngest kid is", kid3) #you can also send arguments with the key = value syntax, the order doesnt matter
keywordfunc(kid3 = "luna", kid2 = "elliot", kid3 = "charlie")

def arbkeyfunc(**kid):
    print("her last name is " + kid[lname]) #this is a combination of keyword and arbitrary functions, activated by putting a **
arbkeyfunc(fname = "kate", lname = "johnson")                                                      #in front of the parameter

def defaultfunc(shape = "spherical"): #this is a default parameter value
    print("my ball is " + shape)
defaultfunc("a prolate spheroid")
defaultfunc() #calling the function with no argument will make it use the default value, which is specified in the brackets

#the data types you send into a function as an argument will always retain their data types
listexample = ["blue", "red", "white"]
def colourfunc(colo):
    for x in colo:
        print(x)
colourfunc(listexample)
print(type(listexample))

def multifunc(x):
    return 5 * x #the return statement lets a function return a value
print(multifunc(8))
print(multifunc(15)) #if you want to see the result you have to print the returned value because the function does not do that

def passfunc():
    pass       #the pass statement can be used to leave a function blank with no error

def positionfunc(x, /): #a forward slash after the parameter means its a postional only argument
    print(x)
def keywordfunc(*, y): #an asterisk before the parameter means its a keyword only argument
    print(y)
positionfunc("hello")
keywordfunc(y = "world")

def combinefunc(a, b, /, *, c, d): #you can combine positional and keyword only arguments, essentially splitting the parameters
    print(a + b + c + d)           #into 2 sections, positional only and keyword only
combinefunc(3, 4, c = 9, d = 10)

#recursion:

def recursionfunc(k):
    if (k > 0):
        calc = k + recursionfunc(k - 1)
        print(calc)
    else:
        calc = 0
    return calc
recursionfunc(6) #this is recursion, it allows a defined function to call itself, meaning you can loop through data to find a result