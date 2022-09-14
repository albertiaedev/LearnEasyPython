'''
Tuples are used to store multiple items in a single variable.
Unlike lists, tuples are unchangeable, allow duplicates and
are written in round brackets.
'''

fruits = ("apple", "banana", "cherry")
print(fruits)

#tuples are indexed as lists do: [0]...[n]
print('------------------')
#tuples allow duplicate values
fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(fruits)

print('------------------')
#tuples can contain many data types: integer, string and boolean
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
print(tuple1,tuple2,tuple3,tuple4)
