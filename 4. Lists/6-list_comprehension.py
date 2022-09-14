'''
List comprehension is a shorter syntax used when you want to
create a new list based on the values of an existing list.
As we have seen before, we can loop through a list with this
simple syntax.
'''

numbers = [1,2,3,4,5,6]
[print(x) for x in numbers]

print('-------------------')

'''
In this example we are printing only the fruits in the list
that have 6 or more letters.
'''

fruits = ["apple","banana","cherry","kiwi","mango",
          "grapes","watermelon","orange","strawberry"]
fruits = [x for x in fruits if len(x)>=6]
print(fruits)
