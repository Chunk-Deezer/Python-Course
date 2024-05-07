class myClass: #created a class named myclass
    x = 5      #property named x
p1 = myClass() #used class named myclass to create objects
print(p1.x)

class Person:
    def __init__(self, name, age): #__init__ function used to assign values to object properties or other necessary operations when
        self.name = name           #the object is being created
        self.age = age
p1 = Person("John", 26)
print(p1.name)
print(p1.age)

class Guy:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):  #the __str__ function is used to control what returns when the object is represented as a string
        return f"{self.name}({self.age})"

p1 = Guy("Joe", 36)
print(p1)

class Fella:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self): #this is a method. a method is a function belonging to an object
        print("My name is " + self.name)

p1 = Fella("Jack", 46)
p1.myfunc()
#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
#it does not have to be called anything specific

class Dude:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("My name is " + self.name)
p1 = Dude("James", 56)
p1.age = 16 #you can modify properties of objects like this
del p1.name #you can properties from objects like this
print(p1.age)
del p1 #you can delete objects with the del keyword like this