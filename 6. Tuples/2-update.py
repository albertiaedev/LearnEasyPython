'''
Tuples are unchangeable.
But there are some workarounds.
'''

#convert a tuple into a list in order to change it
fruits = ("apple","banana","cherry","grapes","lemon","orange")
update = list(fruits)
update[1] = "kiwi"
fruits = tuple(update)
print(fruits)

print('-------------------------')

fruits = ("apple","banana","cherry","grapes","lemon","orange")
update = list(fruits)
update.remove("apple")
fruits = tuple(update)
print(fruits)
