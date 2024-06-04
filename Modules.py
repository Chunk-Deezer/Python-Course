#A module is a set of functions within a file that you want to include in your application
#My module is called MyModule.py

import MyModule as mm #the import statement takes the objects from the module specified and allows them to be referred to here
#the as keyword makes an alias for the module
mm.greeting("Chuck")

a = mm.Fella1["age"] #the Fella1 dict was defined in the module file so after the correct import statment, we can access it here

import platform
x = dir(platform) #the dir function lists all defined objects within the specified module

from MyModule2 import Fella2
#the from keyword allows you to choose what parts to import from a module
print(Fella2["name"]) #since the whole module has not been imported, the module name does not need to be specified