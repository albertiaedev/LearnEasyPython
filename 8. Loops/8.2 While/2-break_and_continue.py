'''
The break statement stops the loop before it has iterated
through all the items and the continue statement stops the
current iteration in the loop and continues to the next one.
'''

#break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print('---------------')

#continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
