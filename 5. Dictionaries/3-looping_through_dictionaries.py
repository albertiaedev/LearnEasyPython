'''
We can loop through a dictionary and obtain the keys
one by one, but there are more method for obtaining values
too, as we can see here.
'''

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)

print('----------------')

#use the .keys() method to get the keys of a dictionary
for key in car.keys():
  print(key)

print('----------------')

#use the .values() method to get the values of a dictionary
for value in car.values():
  print(value)

print('----------------')

#use the .items() method to get both: keys and values
for key, value in car.items():
  print(key, value)
