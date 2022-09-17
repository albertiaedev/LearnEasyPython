'''
The range() function returns a sequence of numbers,
starting from 0 by default, and increments by 1 (by default),
and ends at a specified number.
'''

for x in range(20): #goes from 0 to 19, excluding 20
  print(x)

print('-----------------')

'''
It starts from 0 by default, but it is possible to specify
the starting point just by adding it as a parameter.
'''

for x in range(5, 20): #goes from 5 to 19, excluding 20
  print(x)

print('-----------------')

'''
By default the sequence increments by 1, but it is possible to
specify the sequence by adding it as a third parameter.
'''
for x in range(2, 20, 2): 
  print(x)
