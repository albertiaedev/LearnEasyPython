#looping using a for loop
fruits = ["orange","banana","cherry","grapes"]
for i in range(len(fruits)):
  print(fruits[i])

#looping using a while loop
print('---------------------')
seasons = ["summer","winter","spring","fall"]
i = 0
while i < len(seasons):
  print(seasons[i])
  i = i + 1

#looping with a short syntax using list comprehension
print('---------------------')
numbers = [1,2,3,4,5,6]
[print(x) for x in numbers]
