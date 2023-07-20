#you can loop through items in a list by using a for loop
listz=["lime", "lemon", "orange"]
for x in listz:
    print(x) #this will return the list one by one
for i in range(len(listz)): #this range and len function create a suitable iterable
    print(listz[i]) #this returns the list one by one
thenewlist=["kiwi", "papaya", "passionfruit"]
i = 0
while i < len(thenewlist): #a while loop can be used to loop through the integers 1 by 1
    print(thenewlist[i]) #this returns the list one by one
    i = i + 1
[print(x) for x in thenewlist] #this is a shortened version of using a for loop

betterlist= [x for x in thenewlist if "a" in thenewlist] #this is an easy way to create a new list that is based on another list
print(betterlist) #it is all in one line of code
numberlist=[x for x in range(10) if x>5]#the range function can create an iterable, and a condition only keeps the items that return true
#the expression is the item in the iteration, and you can manipulate the outcome by changing it to anything, it can also be a condition
newlist = [x if x !="papaya" else "banana" for x in thenewlist] #the expression was changed to manipulate the outcome
print(newlist) #this returns a list where papaya is replaced with banana and nothing else changed
#the sort function sorts lists alphanumerically
fruitylist = ("mango", "orange", "banana", "mandarin")
fruitylist.sort() #this sorts the list alphanumerically
print(fruitylist) #this returns the newly sorted list
fruitierlist = ("orange", "mango", "mandarin", "banana")
fruitierlist.sort(reversed = True) #this sorts the list backwards alphanumerically
print(fruitierlist)
#you can customize your function by using key = function 
def myfunc(n):
  return abs(n - 50) #the function will return a number that will be used to sort the list 

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)