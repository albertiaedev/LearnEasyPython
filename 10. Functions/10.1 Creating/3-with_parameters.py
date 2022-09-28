'''
You can also specify the number of parameters that you
desire your function to accept. This will mean that the
function will throw an error if it receives any number of
parameters smaller or greater than the specified.
'''

def function_with_parameters(first_name, last_name):
    print(f"Hello, my name is {first_name} {last_name}")

#when we call it, we have to specify the arguments
function_with_parameters("Alice", "White")
function_with_parameters("Carl", "Blind")
function_with_parameters("Fred", "Jones")

'''
PARAMETER and ARGUMENT are usually used for the same thing,
but from a function's point of view a parameter is the
variable listed inside the parentheses in the function
definition and an argument is the value that is sent to
the function when it is called.
'''
