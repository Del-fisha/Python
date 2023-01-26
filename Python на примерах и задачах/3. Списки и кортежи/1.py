text = tuple(input("Введите текст: "))
dist = int(input("Введите расстояние между индексами: "))
tup = (text[0],)
for i in range(1, len(text)):
    if i % dist == 0:
        tup += (text[i],)

print(tup)
