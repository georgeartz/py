import torch
import numpy as np
import matplotlib.pyplot as plt
x = torch.rand(5, 3)
print(x)
print("\nHi\nHi\nHi")
i = 0
while i < 3:
    print("Loop iteration:", i)
    i += 1
print("\nDone with the loop!")  


arr = np.arange(1, 5)

print(arr)

print(type(arr))

# Matrix multiply example
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
c = torch.matmul(a, b)
print("\nMatrix A:")
print(a)
print("Matrix B:")
print(b)
print("A @ B =")
print(c)

# Graph exp(x) for each element in an array of size n
n = 10
x = np.linspace(0, 3, n)
y = np.exp(x)
print("x = ", x)
print("y = ", y)

plt.plot(x, y, marker='o')
plt.title("exp(x)")
plt.xlabel("x")
plt.ylabel("exp(x)")
plt.grid(True)
plt.show()