'''
You can have if-else statements inside if-else statements,
this is called nested if-else statements.
'''

num = 50

if num > 10:
  print("Your number is above 10...")
  if num > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
else:
    print("Your number is not greater than 10...")
