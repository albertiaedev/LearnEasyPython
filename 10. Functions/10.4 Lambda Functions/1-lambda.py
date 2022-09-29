'''
A lambda function is a small anonymous function that can take any number of arguments
but can have only one expression.
'''

x = lambda a : a + 10
print(x(5)) 

print("---------")

x = lambda a, b : a * b
print(x(5, 6))

'''
The power of lambda is better shown when you use them as an anonymous
function inside another function.
Say you have a function definition that takes one argument,
and that argument will be multiplied with an unknown number:
'''

def myfunc(n):
  return lambda a : a * n 
  
print("---------")

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
