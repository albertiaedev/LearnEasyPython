'''
An conditional statement is used to determine whether a condition
is met or not. This time, we'll talk about the if statement, which
is written using the if keyword and accepts all types of operators:
arithmetic, relational and logical.
'''

a = 50
b = 100
if b > a:
  print("b is greater than a") #move print() with indentation
                               #this is done using 2-4 spaces

print('-------------------')

a = 50
b = 100
if b == a:
  print("b is equal to a") #move print() with indentation
                           #this is done using 2-4 spaces

#you have to use indentation, instead of the typical curly brackets
print('-------------------')

a = 50
b = 100
if b == a:
print("b is equal to a") #otherwise you'll get an error
