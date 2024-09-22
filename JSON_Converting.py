
# Parse JSON - Convert from JSON to Python
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# Convert from Python to JSON
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "3": 5
}

# convert into JSON:
y = json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True)

# the result is a JSON string:
print(y)

