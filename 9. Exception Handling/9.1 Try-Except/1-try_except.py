'''
When an error occurs, or exception as we call it,
Python will normally stop and generate an error message.
These exceptions can be handled using the try-except statement.
'''

#it throws an error because x is not defined
try:
  print(x)
except:
  print("An exception occurred")

print('-----------------------')

'''
You can define as many exception blocks as you want, if you want
to execute a special block of code for a special kind of error.
Next code prints one message if the try block raises a NameError
and another for other errors.
'''

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
