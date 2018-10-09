old_list = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]

new_list = []

def func(temp_list):
    for i in temp_list:
        if type(i) == tuple:
            func(i)
        if type(i) == list:
            func(i)
        else :
            new_list.append(i)

func(old_list)


print(old_list)
print(new_list)

