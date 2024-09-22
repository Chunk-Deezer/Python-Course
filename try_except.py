"""The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks."""

try:
    print(x)
except:
    print("an exception has occurred")

# secific errors e.g. NameError
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong") 

# You can use the else keyword to define a block of code to be executed if no errors were raised:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") 

#finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") 

#example
"""try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file") """

#raise
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed") 