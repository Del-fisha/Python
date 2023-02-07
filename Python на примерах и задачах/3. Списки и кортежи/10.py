import random

array_1 = []
array_2 = []
array_3 = []

for i in range(11):
    array_1.append(random.randint(10, 20))
for i in range(11):
    array_2.append(random.randint(10, 20))

for i in range(len(array_1)):
    array_3.append(array_1[i])
    array_3.append(array_2[i])

print(array_1)
print(array_2)
print(array_3)
