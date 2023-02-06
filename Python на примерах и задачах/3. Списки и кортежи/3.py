import random


def random_ch(col, raw):
    array = [[chr(random.randint(65, 90)) for i in range(col)] for j in range(raw)]
    for a in array:
        for b in a:
            print(b, end=" ")
        print()


random_ch(4, 5)
