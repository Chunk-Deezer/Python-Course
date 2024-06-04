#Scope defines the range the variable is recognised within, for example the variable on line 2 is a local variable in the local scope
x = "Global func variable definition"

def outerfunc():
    x = "Outer func (local) variable definition"
    def innerfunc():
        nonlocal x      #The nonlocal keyword makes it so that the variable belongs to the outer function
        x = "Inner func (local) variable definition"  #this ^ only works in nested functions
    innerfunc()
    return x  #this will return the inner func variable definition

print(outerfunc()) 

y = "original variable definiton"
def myfunc():
    global y     #the global keyword makes it so you can change the global variable definition within a function
    y = "changed variable definition" #also if there was not already a global variable called 'y' then it would create one

myfunc()
print(y) #print within the global scope because the global variable was changed, a local variable within that function doesn't exist