import numpy as np

a = np.array([2,5,8,8,5,6])

print(a)

#array size
print(f'array size: {a.size}')
#array dimension
print(f'array dimension: {a.ndim}')
#array type
print(f'array type: {a.dtype}')
#array dimension and elements
print(f'array dimension and elements: {a.shape}\n')

"Array Elements"
print("Array Elements")
arr = np.array([1, 2, 3, 4])

print(f'{arr[1]}\n')

"Array slicing"
print("Array slicing")
ar = np.array([1, 2, 3, 4, 5, 6, 7])

print(f'{ar[1:5]}\n')

"Copy and View"
print("Copy and View \n")
print("Copy")
c = np.array([1, 2, 3, 4, 5])
x = arr.copy()
c[0] = 42

print(c)
print(f'{x}\n')

print('View')
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

"Operations - Arrays"
print("Operations - Arrays")
#addition
b = np.array([2,5,8,8,5,6])

sum = b+10
print(sum)
print('\n')
#subtraction

#multiplication 

#division