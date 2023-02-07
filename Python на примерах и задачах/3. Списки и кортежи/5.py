import random

column = int(input("Введите ширину матрицы: "))
rows = int(input("Введите высоту матрицы: "))
array = [[random.randint(0, 10) for col in range(column)]for row in range(rows)]

for i in array:
    for j in i:
        print(str(j).rjust(2), end=" ")
    print()

del_row = int(input("Какую строку удалить? \n"))
for i in range(len(array)-1):
    if i == del_row:
        array.pop(i)

for i in array:
    for j in i:
        print(str(j).rjust(2), end=" ")
    print()

del_column = int(input("Какую колонку удалить? "))

for i in array:
    for j in range(len(i)-1):
        if j == del_column:
            i.pop(j)

for i in array:
    for j in i:
        print(str(j).rjust(2), end=" ")
    print()