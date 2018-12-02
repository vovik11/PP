from collections import deque

def WriteLines(n):
    with open("a.txt") as k:
        for row in deque(k, n):
            print(row.strip())


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
