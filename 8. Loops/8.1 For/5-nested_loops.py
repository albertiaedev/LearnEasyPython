'''
A nested loop is a loop inside a loop that executes one
time for each iteration of the first loop.
'''

adj = ["good","big","tasty","juicy","acid"]
fruits = ["apple","banana","cherry","grapes","lemon"]

for x in adj:
  for y in fruits:
    print(x, y)
