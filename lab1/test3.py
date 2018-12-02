num1 = int()
num2 = int()
a = int(input('Enter num1:\n '))
b = int(input('Enter num2:\n'))

def func(num1,num2):
    if num1 < 0:
        raise Exception ('Error!')

    if num2 < 0:
        raise Exception ('Error!')

    if num1 % num2 == 0:
        res = bool(1)
        print(res)
        return res
    else:
        res = bool(0)
        print(res)
        return res


func(a,b)