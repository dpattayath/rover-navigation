
class Rover:
    """
    Class that represents Rover
    - represented as x, y coordinates and cardinal direction
    """
    def __init__(self, x: int, y: int, cardinal: str):
        self.cardinal = cardinal
        self.x_coord = x
        self.y_coord = y
        self.max_x_coord = None
        self.max_y_coord = None
        self.min_x_coord = 0
        self.min_y_coord = 0
        self.cardinal_directions = {
            'left': {
                'N': 'W',
                'W': 'S',
                'S': 'E',
                'E': 'N'
            },
            'right': {
                'N': 'E',
                'W': 'N',
                'S': 'W',
                'E': 'S'
            }
        }

    def move(self):
        """
        Handles the move action of the rover
        """
        if self.cardinal == 'N' and not self.max_y_coord == self.y_coord:
            self.y_coord += 1
        elif self.cardinal == 'E' and not self.max_x_coord == self.x_coord:
            self.x_coord += 1
        elif self.cardinal == 'S' and not self.min_y_coord == self.y_coord:
            self.y_coord -= 1
        elif self.cardinal == 'W' and not self.min_x_coord == self.x_coord:
            self.x_coord -= 1

    def set_max_coordinates(self, x: int, y: int):
        """
        Sets the max coordinates. feed by the plateau thats being navigated
        """
        self.max_x_coord = x
        self.max_y_coord = y

    def left(self):
        """
        Handles the left turn action of the rover
        """
        self.cardinal = self.cardinal_directions['left'][self.cardinal]

    def right(self):
        """
        Handles the right turn action of the rover
        """
        self.cardinal = self.cardinal_directions['right'][self.cardinal]

    def show_position(self):
        """
        Handles printing the current position of the rover
        """

        print(f"Position after navigation: {self.x_coord}, {self.y_coord}, {self.cardinal}")

    def send_command(self, command: str):
        if command == 'L':
            self.left()
        elif command == 'R':
            self.right()
        else:
            self.move()


