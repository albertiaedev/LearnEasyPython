'''
You can index an item in a list by the items
index number.
The indexation starts with [0] and follows n numbers in the list.
'''

fruits = ['apple','banana','orange','grapes','lemon']
print('The fruits list contains:',fruits)
print('This is item Nº1:',fruits[0])
print('This is item Nº2:',fruits[1])
print('This is item Nº3:',fruits[2])
print('This is item Nº4:',fruits[3])
print('This is item Nº5:',fruits[4])

print('---------------------------')

cars = ['toyota','ford','chevrolet','hyundai','volkswagen']
print('The cars list contains:',cars)
print('This is item Nº1:',cars[0])
print('This is item Nº2:',cars[1])
print('This is item Nº3:',cars[2])
print('This is item Nº4:',cars[3])
print('This is item Nº5:',cars[4])

'''
Negative indexation can be done, where we use -1 for the last item
in the list, and so on.
'''
print('---------------------------')

colors = ['red','blue','yellow','green','purple']
print('The colors list contains:',colors)
print('This is item Nº1:',colors[-5])
print('This is item Nº2:',colors[-4])
print('This is item Nº3:',colors[-3])
print('This is item Nº4:',colors[-2])
print('This is item Nº5:',colors[-1])

print('---------------------------')

#slicing through list is done as follows:

print(fruits[1:4]) #extracts items including [1] and excluding [4]
print(cars[0:]) #extracts items including [0] to the last
print(colors[:4]) #extracts items from the first excluding [4]
