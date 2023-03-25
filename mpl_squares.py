import matplotlib.pyplot as plt
import traceback

input_values = [1, 2, 3, 4, 5]
squares = []
for value in input_values:
    squares.append(value*value)
#squares = input_values*input_values
#squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8-darkgrid')

fig,ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)
ax.set_title("Square numbers")
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

ax.tick_params(axis='both', labelsize=14)

plt.show()
