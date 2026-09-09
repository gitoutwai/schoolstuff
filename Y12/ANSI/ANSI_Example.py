# ANSI Example
# https://en.wikipedia.org/wiki/ANSI_escape_code
# https://www.compart.com/en/unicode/search?q=box+drawing#characters

import sys

# Draw a box
def draw_box(width, height, makeSquare, coords):

    # Saves current location
    sys.stdout.write("\033[s")

    # Move to coords
    stringCoords1 = str(coords[1])
    sys.stdout.write(f"\033[{stringCoords1}B")

    box_parts = {"TL":"╔", "TR":"╗", "BL":"╚", "BR":"╝", "V":"║", "H":"═"}

    if makeSquare:
        width *= 2
    width += coords[0]

    for y in range(height):
        for x in range(width):
            if width == 1 and height == 1:
                print("■")
            # TL
            elif x == 0+coords[0] and y == 0:
                print(box_parts["TL"], end="")
            # TR
            elif x == width - 1 and y == 0:
                print(box_parts["TR"], end="")
            # BL
            elif x == 0+coords[0] and y == height - 1:
                print(box_parts["BL"], end="")
            # BR
            elif x == width - 1 and y == height - 1:
                print(box_parts["BR"], end="")
            # Ver
            elif x == 0+coords[0] or x == width - 1:
                print(box_parts["V"], end="")
            # Hor
            elif (y == 0 or y == height - 1) and x >= 0+coords[0]:
                print(box_parts["H"], end="")
            # Empty
            else:
                sys.stdout.write("\033[C")
        print()

    # Return to saved spot
    sys.stdout.write("\033[u")

# use function
coords = [0,0]
draw_box(4,4, makeSquare=True, coords=coords)

coords = [2,2]
draw_box(2,2, makeSquare=True, coords=coords)

sys.stdout.write("\033[100A")

# Cursor

# Cursor ANSI escape code
# Homework
# Make the box draw in the right place
# Allow coordinates so that they can draw inside of each other.