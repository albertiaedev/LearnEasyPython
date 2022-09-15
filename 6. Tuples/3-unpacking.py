'''
Unpacking a tuple means that we can extract each of these
values and put it into another variable.
'''

fruits = ("apple","banana","cherry")
(aaa, bbb, ccc) = fruits
print(aaa)
print(bbb)
print(ccc)

print('-------------------')

'''
If the number of variables is less than the number of values,
you can add an * to the variable name and the values will be
assigned to the variable as a list.
'''

groceries = ("milk","oil","eggs","mustard","meat","cheese","rice")
(aaa, bbb, *ccc) = groceries
print(aaa)
print(bbb)
print(ccc)
