array = [11, 3, 1, 6, 4, 10, 2, 8, 9, 7, 0, 5]
step = 1
for i in range(len(array)-step):
    for j in range(len(array) - 1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
    step += 1

print(array)