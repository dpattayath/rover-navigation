from rover import Rover
from plateau import Plateau

"""Process rover instructions accepting user input
"""
def rover_instructions(plane: Plateau, rover_info: str):
    pos_x, pos_y, direction = rover_info.split(' ')
    commands = input("Enter nav instructions: ")

    rover = Rover(int(pos_x), int(pos_y), direction)
    plane.add_rover(rover)

    for command in commands:
        rover.send_command(command)
    rover.show_position()

if __name__ == "__main__":

    try:
        # get plateau coordinates from user
        plateau_info = input("Enter max coordinates for plateau [x y]:")
        max_x, max_y = plateau_info.split(' ')
        plane = Plateau(int(max_x), int(max_y))

        while True:
            rover_info = input("Enter current position of rover [x y direction]: ")
            if rover_info == "end":
                plane.show_grid()
                break
            rover_instructions(plane, rover_info)
    except BaseException as e:
        print(f"Error processing request: {e}")
