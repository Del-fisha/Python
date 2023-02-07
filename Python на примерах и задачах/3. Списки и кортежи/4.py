size = int(input("Введите размер стороны матрицы: "))
array = [[0 for i in range(size)] for j in range(size)]
def snake(arr):
    s = 1
    x = 0
    y = -1
    d_row = 1
    d_column = 0
    length = len(str(size ** 2))
    while s <= size ** 2:
        if 0 <= x + d_row < size and 0 <= y + d_column < size and array[x + d_row][y + d_column] == 0:
            x += d_row
            y += d_column
            array[x][y] = s
            s += 1
        else:
            if d_row == 1:
                d_column = 1
                d_row = 0
            elif d_column == 1:
                d_row = -1
                d_column = 0
            elif d_row == -1:
                d_column = -1
                d_row = 0
            elif d_column == -1:
                d_row = 1
                d_column = 0

    for i in arr:
        for j in i:
            print(str(j).rjust(length), end=" ")
        print()


snake(array)
