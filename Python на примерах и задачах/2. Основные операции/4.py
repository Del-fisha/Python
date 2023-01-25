array_1 = [1, 2, 34, 56, 789]
array_2 = [1, 2, 34, 56, 789]
count = 0
for i in range(len(array_1)):
    if array_1[i] == array_2[i]:
        count += 1
        i += 1
if count == len(array_1) and count == len(array_2):
    print("Списки равны")
else:
    print("Списки не равны")
