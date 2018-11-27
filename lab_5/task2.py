import numpy as np

def func(z, A):
    index = (np.abs(A - z)).argmin()
    return A[index]

M = 208
N = 20
mass = np.zeros((M, N))
print(mass)

a = np.array([1, 3, 10])

key = int(input('Enter key:'))
print(key)





print(func(key, a))