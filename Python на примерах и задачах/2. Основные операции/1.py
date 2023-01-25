num = input("Введите целое число: ")

for i in range(9):
    count = 0
    for j in num:
        if i == int(j):
            count += 1
    if count > 0:
        print(f"Цифра {i} встречается в Вашем числе {count} раз")
