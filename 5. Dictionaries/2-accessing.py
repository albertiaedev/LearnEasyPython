'''
We can access to an item in a dictionary just by enetering
its key name between square brackets.
'''

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
model = car["model"]
print(model)

print('----------------')

#there's also a method called .get() that gives the same result

model = car.get('model')
print(model)

print('----------------')

#the .keys() method will return a list of the keys in a dictionary

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
keys = car.keys()
print(keys)
