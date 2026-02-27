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

dy = np.diff(y) / np.diff(x)
x_mid = (x[:-1] + x[1:]) / 2  # midpoints for plotting
print("dy/dx = ", dy)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

ax1.plot(x, y, marker='o')
ax1.set_title("exp(x)")
ax1.set_xlabel("x")
ax1.set_ylabel("exp(x)")
ax1.grid(True)

ax2.plot(x_mid, dy, marker='o', color='orange')
ax2.set_title("d/dx exp(x)")
ax2.set_xlabel("x")
ax2.set_ylabel("dy/dx")
ax2.grid(True)

plt.tight_layout()
plt.show()