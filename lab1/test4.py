a = int()
b = int()
num1 = int(input('Enter num1: \n'))
num2 = int(input('Enter num2: \n'))
def task4(a, b):
    if (a > b):
        a, b = b, a
    x = []
    for i in range(a, b + 1):
        if i > 0:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                x.append(i)
    if x != []:
        print(x)
        return x
    else:
        raise Exception('Error!')

task4(num1, num2)