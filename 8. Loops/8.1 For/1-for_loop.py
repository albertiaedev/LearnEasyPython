'''
A for loop is used for iterating through data structures such
as lists, dictionaries, tuples or strings. It means it will go
through the data structure and print every item in it.
'''

#looping through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print('---------------')

#looping through a dictionary
car = {'Brand':'Ford','Model':'Mustang','Year':2007}
for x in car:
  print(car[x])

print('---------------')

#looping through a tuple
fruits = ("apple", "banana", "cherry")
for x in fruits:
  print(x)

print('---------------')

#looping through a string
for x in "banana":
  print(x)
