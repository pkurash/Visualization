import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    
    # plt.style.use('classic')
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens,
        edgecolors = 'none', s = 15)

    ax.scatter(rw.redx, rw.redy, c = 'red', s=200, linestyle="solid")
    ax.plot(rw.redx, rw.redy, c = 'red', linestyle="solid")
    
    for i in range(len(rw.rlbl)):
        ax.annotate(rw.rlbl[i], (rw.redx[i]+4, rw.redy[i]+4))

    plt.show()
    plt.savefig('Random_walk_plot.png', bbox_inces='tight')
   
    break
#    keep_running = input("Make another walk? (y/n):")
#    if keep_running == 'n':
#        break
