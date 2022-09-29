'''
The self parameter is a reference to the current instance of the class,
and is used to access variables that belongs to the class.
It does not have to be named self, you can call it whatever you like,
but it has to be the first parameter of any function in the class.
'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

object = Person("John", 36)
object.myfunc() 
