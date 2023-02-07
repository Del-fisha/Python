import random

array = []
array_even = []
array_odd = []
for i in range(10):
    array.append(random.randint(1, 20))
print(array)

for i in range(0, len(array)-1, 2):
    array_even.append(array[i])
    array_even.sort()

for i in range(1, len(array), 2):
    array_odd.insert(i, array[i])
    array_odd.sort(reverse=True)

for i in range(1, len(array), 2):
    array_odd.insert(i, 0)

array = []
for i in range(len(array_even)):
    array.insert(i, array_even[i])
for i in range(0, len(array_odd), 2):
    array.insert(i, array_odd[i])

print(array)
