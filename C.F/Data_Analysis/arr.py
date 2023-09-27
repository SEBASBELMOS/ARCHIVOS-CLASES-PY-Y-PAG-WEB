import numpy as np

a = np.random.randint(0,10,20)

print(a)

def operation(value):
    return (value ** 2) + 2

print(operation(3))

for value in a:
    operation(value)
    
for value in a:
    print(operation(value))
    
vector = np.vectorize(operation)

vector(a)

vector = np.vectorize(lambda value: (value **2)+2)