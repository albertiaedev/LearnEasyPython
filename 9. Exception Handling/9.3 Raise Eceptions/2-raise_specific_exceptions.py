
'''
You can define what kind of error to raise,
and the text to print to the user
'''

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
