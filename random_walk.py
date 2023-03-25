from random import choice

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points
    
        """All walks start at (0,0)"""
        self.x_values = [0]
        self.y_values = [0]

        self.redx = [0]
        self.redy = [0]
        self.rlbl = ['0']

    def fill_walk(self):
        """"Calculate all the points in the walk"""
         
        while  len(self.x_values)  < self.num_points:

            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #Reject moves that go nowhere
            if x_step and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

            if len(self.x_values)  % 1000 == 0:
                self.redx.append(x)
                self.redy.append(y)
                self.rlbl.append(str(len(self.x_values)))
