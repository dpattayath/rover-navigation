
from rover import Rover

class Plateau:
    """
    Class that represents Plateau
    - holds the rovers
    - represented as coordinates
    """

    def __init__(self, x:int, y:int):
        self.upper_x_coord = x
        self.upper_y_coord = y
        self.rovers = []
        self.coordinates = [[0 for x in range(self.upper_x_coord + 1)] for y in range(self.upper_y_coord + 1)]

    def add_rover(self, rover: Rover):
        """
        Set max coordinates on the rover and add rover to the plateau
        """
        rover.set_max_coordinates(self.upper_x_coord, self.upper_y_coord)
        self.rovers.append(rover)

    def show_grid(self):
        """
        Handles showing the plateau as a grid
        """
        for key, rover in enumerate(self.rovers):
            self.coordinates[rover.x_coord][rover.y_coord] = key + 1

        for row in self.coordinates:
            print(row)
