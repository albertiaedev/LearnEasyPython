'''
Dictionaries are data structures used for storing data in
the form of key:value pairs and they're written in curly
brackets.
'''

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)

print('----------------')

#items in a dictionary can be of any type
car =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(car)

print('----------------')

#we use len() to determine how many items a dictionary has
print(len(car))

print('----------------')

#dictionaries are defined as objects with the data type 'dict'
print(type(car))
