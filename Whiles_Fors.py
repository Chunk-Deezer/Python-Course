#while loop executes the code contained within as long as the condition is true
numero = 1
while numero < 8:
    if numero == 2:
        continue        #the continue statement skips to the next iteration 
    if numero == 6:
        break        
    print(numero)       #the break statement stops the loop even if the condition is true
    numero = numero + 1 #if i did not increment the variable the loop would have gone infinitely
else:
    print("numero has become 8") #you can use elses with while loops and they execute when the condition is no longer true
#for loop is used for iterating over a sequence
word = "pineapple"
count = 0
for x in word: #for each letter in the variable, word, count will increase, counting how many letters in the word
    count = count + 1
print(count)
#this will be the same with arrays but will count items not letters
for x in word:
    if x == "p":
        continue     #the continue statement will jump to the next iteration just like in a while loop
    if x == "l":
        break        #the break statement will stop the loop regardless, just like in a while loop
    print(x) #if the break was after the print, it would still print the letter l

for x in range(1, 60, 10): #the 3rd number acts as the number the list created increments by and the other two act as a specified range
    print(x)       #this makes it perfect for looping code with a for loop for a specified number of times
else:
    print("done") #elses can be used after for loops, it executes when all iterations are finished
 #the range function returns a set of numbers starting  0 (default), incrementing by 1 (default) and stopping at 1 before the number
numone = [1, 2, 3]
numtwo = [4, 5, 6]
for x in numone:
    for y in numtwo: #this is a nested if, an if in an if
        print(x,y)

if 8 == 3:
    pass #the pass statement is used to avoid an error if you have an empty if 