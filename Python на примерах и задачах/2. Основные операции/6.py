first = int(input("Введите длину первой стороны: "))
second = int(input("Введите длину второй стороны: "))
third = int(input("Введите длину третьей стороны: "))

if first + second > third and third + first > second and second + third > first:
    print("Треугольник с такими сторонами существует")
else:
    print("Треугольник с такими сторонами не существует")