array = [2, 5]
number = int(input("Введите верхнюю границу: "))
count = 0
for i in range(number + 1):
    if i not in array:
        count += i
print(count)
