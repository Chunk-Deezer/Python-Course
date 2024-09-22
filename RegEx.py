import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

# findall
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) 

# search
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x) 

#split()
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x) 

# sub()
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#match object
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x.group()) #this will print an object

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span()) 

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) 

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) 