'''
In order to add an item to a dictionary we just have to
create a new index key and assing a value to it.
'''

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
print(car)

print('-----------------')

#use the .update() method to update the dictionary
car.update({"color": "green"})
print(car)

print('-----------------')

'''
There are several methods to remove items from a dictionary,
her we are going to talk about the principal.
'''

#use the .pop() to remove an item with the specified key name
car.pop("year")
print(car)

print('-----------------')

#use the .clear() to empty a dictionary
car.clear()
print(car)
