# ANSI Example
# https://en.wikipedia.org/wiki/ANSI_escape_code
# https://www.compart.com/en/unicode/search?q=box+drawing#characters

import sys
import os

def clear():
    """
    Clear the screen
    """

    print("\x1b[3J", end="")

def move_to(coords):
    # Move to coords
    if coords[1] > 0:
        y = str(coords[1])
        sys.stdout.write(f"\033[{y}B") # Moves down

    # x = str(coords[1])
    # sys.stdout.write(f"\033[{x}C") # Moves right

# Draw a box
def draw_box(width, height, coords, makeSquare=False, modifier="H"):

    move_to(coords)

    box_parts = {"HTL":"╔", "HTR":"╗", "HBL":"╚", "HBR":"╝", "HV":"║", "HH":"═"}

    if makeSquare:
        width *= 2
    width += coords[0]

    for y in range(height):
        for x in range(width):
            if width == 1 and height == 1:
                print("■")
            # TL
            elif x == 0+coords[0] and y == 0:
                print(box_parts[f"{modifier}TL"], end="")
            # TR
            elif x == width - 1 and y == 0:
                print(box_parts[f"{modifier}TR"], end="")
            # BL
            elif x == 0+coords[0] and y == height - 1:
                print(box_parts[f"{modifier}BL"], end="")
            # BR
            elif x == width - 1 and y == height - 1:
                print(box_parts[f"{modifier}BR"], end="")
            # Ver
            elif x == 0+coords[0] or x == width - 1:
                print(box_parts[f"{modifier}V"], end="")
            # Hor
            elif (y == 0 or y == height - 1) and x >= 0+coords[0]:
                print(box_parts[f"{modifier}H"], end="")
            # Empty
            else:
                sys.stdout.write("\033[C")
        sys.stdout.write("\033[B")

# Cursor

# Cursor ANSI escape code
# Homework
# Make the box draw in the right place
# Allow coordinates so that they can draw inside of each other.

if __name__ == "__main__":

    terminal_width = os.get_terminal_size()[0]
    terminal_height = os.get_terminal_size()[1]

    # use function

    clear()

    # Saves current location
    sys.stdout.write("\033[s")

    coords = [0,0]
    draw_box(width=terminal_width-1,height=terminal_height-5, makeSquare=False, coords=coords)

    # Return to saved spot
    sys.stdout.write("\033[u")

    coords = [0,terminal_height-1]
    draw_box(terminal_width,5, coords=coords)

    sys.stdout.write("\033[100A")
    input()