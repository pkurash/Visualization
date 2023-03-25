import matplotlib.pyplot as plt

#set x and y values
x_values = range(1, 11)
y_values = [x**2 for x in x_values]

fig,ax = plt.subplots()
ax.scatter(x_values, y_values, s = 10, cmap=plt.cm.Blues)

plt.style.use('seaborn-v0_8-darkgrid')

#set x and y axes
ax.set_title("Square numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

ax.tick_params(axis='both', labelsize=14)

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()

