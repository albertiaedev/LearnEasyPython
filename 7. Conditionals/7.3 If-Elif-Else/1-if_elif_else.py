'''
The elif keyword is pythons way of saying "if the previous
conditions were not true, then try this condition".
'''

a = 200
b = 300
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#you can have as many elif statements as you want
num = 200

if num >= 1 and num <= 100:
  print("The number is 1-100.")
elif num >= 101 and num <= 150:
  print("The number is 101-150.")
elif num >= 151 and num <= 175:
   print("The number is 151-175.")
elif num >= 176 and num <= 200:
  print("The number is 176-200.")
else:
  print("The number is not known.")
