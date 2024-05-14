class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe") #using the person class to create an object
x.printname() #executing printname method

class Student(Person): #this class named student inherits the functionality from another class, because the parent class is the 
    pass                                                                                                              #parameter

y = Student("Glenn", "Turner") #the student class has the exact same properties and methods as the Person class
y.printname()

class student(Person):
    def __init__(self, fname, lname): #when the __init__ function is added the child will no longer inherent the parent's __init__ func
        Person.__init__(fname, lname) #to keep the inheritance of the parent's __init__ function, a call to the parent's __init__
                                                                                                           #function must be made
#now the child class has the __init__ function and has kept the inheritance of the Person class it can be used to add functionality
#there is also a super() function which will make the child class inherit all methods and properties from its parent without having
#to name the parent specifically. it is used in the same place as Person is

class student2(Person):
    def __init__(self, fname, lname, year): #year parameter must be added for property below
        super().__init__(fname, lname)
        self.year = year #added property called year
    def welcome(self): #method called welcome
        print("welcome", self.firstname, self.lastname, "to the class of", self.year)
z = student2("Johnny", "Sins", 1994) #the year 1994 is a variable passed into the student class while creating the object

#if you create a method in the child class that shares its name with a function in the parent class, the inheritance of the parent
#class will be overriden