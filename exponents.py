import matplotlib.pyplot as plt
import numpy as np
print(np.e)

fig, ax = plt.subplots()  # Create a figure containing a single axes.

exponents_1 = []
exponents_2 = []

result_list = []

n = 0.9
while n > 0:
    if n < 1:
        exponents_1.append(n)
        result = pow(n, n)
        result_list.append(result)
        print(f'{round(n, 2)}^{round(n, 2)} = {result}')

        n -= 0.01

i = 0
for x in exponents_1:
    exponents_2.append(exponents_1[-1-i])
    i += 1
print(exponents_1)
print(exponents_2)

ax.plot(exponents_1, result_list)  # Plot some data on the axes

ax.plot(1 / np.e, pow(1 / np.e, 1 / np.e), marker="o", markersize=6, markerfacecolor="green")


plt.show()
