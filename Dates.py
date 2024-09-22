import datetime #datetime module
timenow = datetime.datetime.now() 
print(timenow) #displays current year, month, day, hour, minute, second and microsecond in that order
print(timenow.year) #returns current year
print(timenow.strftime("%A")) #returns current weekday

dateobject = datetime.datetime(2024, 7, 6) #this creates a date object