import random

array = []

for i in range(10):
    array.append(random.randint(1, 20))
print(array)

for j in range(0, (len(array)-1) * 2, 2):
    summ = array[j] + array[j + 1]
    array.insert(j + 1, summ)

print(array)
