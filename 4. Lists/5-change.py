#we refer to the item index to change a specific item
fruits = ["apple","banana","cherry","grapes","lemon"]
fruits[1] = "orange"
print(fruits)

print('-----------------')

#we can also change a range of indexes through slicing
fruits = ["apple","banana","cherry","grapes","lemon"]
fruits[0:2] = ["orange","watermelon"]
print(fruits)

print('-----------------')

#change the first value by replacing it with two new values
fruits = ["apple","banana","cherry","grapes","lemon"]
fruits[0:1] = ["orange","watermelon"]
print(fruits)

print('-----------------')

#change the first  and the secondvalue by replacing it with one value
fruits = ["apple","banana","cherry","grapes","lemon"]
fruits[0:2] = ["orange"]
print(fruits)
