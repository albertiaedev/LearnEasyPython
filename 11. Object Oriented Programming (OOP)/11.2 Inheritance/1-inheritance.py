'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.

A PARENT CLASS is the class being inherited from, also called base class.

A CHILD CLASS is the class that inherits from another class, also called derived class
'''

#CREATE A PARENT CLASS
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

object = Person("John", "Doe")
object.printname()

print('----------------------')

#CREATE A CHILD CLASS
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
