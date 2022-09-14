'''
We use the .append() method to add a new item to a list.
We have to remember that items are always added to the last
index in the list.
'''

decades = ["'10","'20","'30","'40","'50","'60","'70","'80","'90"]
decades.append("'00")
print(decades)

print('--------------------')

#we use the .insert() method to insert an item at a specified index
fruits = ["apple","banana","cherry","grapes","lemon"]
fruits.insert(2,"orange")
print(fruits)

print('--------------------')

#we use the .extend() method to add elements from another list
fruits = ["apple","banana","cherry","orange"]
tropical = ["mango","pineapple","papaya","guayaba"]
fruits.extend(tropical)
print(fruits)

print('--------------------')

#we use the .remove() method to remove a specified item
decades = ["'10","'20","'30","'40","'50","'60","'70","'80","'90"]
decades.remove("'10")
print(decades)

print('--------------------')

#we use the .pop() method to remove a specified index
fruits = ["apple","banana","cherry","grapes","lemon"]
fruits.pop(2)
print(fruits)

print('--------------------')

#we use the .clear() method to empty a list
numbers = [1,2,3,4,5,6]
numbers.clear()
print(numbers)
