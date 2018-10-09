from collections import deque

def WriteLines(n):
    f = open("a.txt", 'r')
    with open("a.txt") as k:
        for row in deque(k, n):
            print(row.strip())

    f.close()


# та записує парні рядки у Верхньому регістрі в файл b1
# а непарні в нижньому регістрі в файл b2
def separ():
    f = open("a.txt", 'r')
    wparn = open('b1.txt', 'w')
    wneparn = open('b2.txt', 'w')
    for index, line in enumerate(f):
        if index % 2 == 0:
            wparn.write(line.upper())
        else:
            wneparn.write(line.lower())
    wparn.close()
    wneparn.close()
    f.close()


a = int(input("Enter number: "))
WriteLines(a)

separ()
