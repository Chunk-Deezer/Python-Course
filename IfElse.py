import random
a = random.randint(1,10)
b = random.randint(1,10)
if a > b: #you can compare variables with logical conditions #example of if statement #IT HAS TO BE INDENTED
    print("a is bigger than b") 
elif a < b: #example of an elif statment, means 'try these conditions next if the previous were not true'
    print("b is bigger than a")
else: #an else statement just catches anything not caught in preceeding conditions
    print("b is equal to a")
c = 33
if c == 33: print("c is equal to 33") #short hand if - if there is only 1 statement to execute, it can be on the same line
print("c is 22") if c == 22 else print("c is not 22") #this short hand if else is an example of a ternary operator 
d = 52
print("d = 42") if d == 42 else print("d is 52") if d == 52 else print("d is not 42 nor 52") #triple condition shorthand if else
e = 3
f = 4
g = 5
if not e > f or f > g and g < e: #not, or, and can all be used in if statements 
    print("either f is bigger than e or g is bigger than f or both the previous statments are true AND g is bigger than e")
number = random.randint(1,50)
if number > 10:
    print("this number is more than ten,")
    if number > 20:
        print("and more than 20,")
        if number > 30: #these if statements are examples of nested ifs and its just an if in an if
            print("and more than 30,")
            if number > 40:
                print("and more than 40!")
            else:
                print("but less than 40.")
        else:
            print("but less than 30.")
    else:
        print("but less than 20.")
if number >= 1:
    pass #you can use the pass statement to avoid getting an error for no content in an if, if that is needed