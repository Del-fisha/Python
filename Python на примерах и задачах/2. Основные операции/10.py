print("Ax = B - A - 1")
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
x = 0

if a != 0:
    x = (b-1)/a-1
    print(x)
if a == 0 and b == 1:
    print("Решение - любое число")
if a == 0 and b != 1:
    print("Решения нет")

