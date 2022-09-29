'''
If you do not know how many arguments that will be passed into your function,
add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:
'''

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") 
