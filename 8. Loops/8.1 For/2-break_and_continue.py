'''
The break statement stops the loop before it has iterated
through all the items and the continue statement stops the
current iteration in the loop and continues to the next one.
'''

#break
fruits = ["apple","orange","grapes","banana","cherry","lemon"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print('---------------')

#continue
fruits = ["apple","orange","grapes","banana","cherry","lemon"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
