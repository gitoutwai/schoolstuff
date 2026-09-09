# ANSI Example
# https://en.wikipedia.org/wiki/ANSI_escape_code
# https://www.compart.com/en/unicode/search?q=box+drawing#characters

# Draw a box
def draw_box(width, height, makeSquare, coords):

    box_parts = {"TL":"╔", "TR":"╗", "BL":"╚", "BR":"╝", "V":"║", "H":"═"}

    if makeSquare:
        width *= 2

    for y in range(height):
        for x in range(width):
            if width == 1 and height == 1:
                print("■")
            # TL
            elif x == 0 and y == 0:
                print(box_parts["TL"], end="")
            # TR
            elif x == width - 1 and y == 0:
                print(box_parts["TR"], end="")
            # BL
            elif x == 0 and y == height - 1:
                print(box_parts["BL"], end="")
            # BR
            elif x == width - 1 and y == height - 1:
                print(box_parts["BR"], end="")
            # Ver
            elif x == 0 or x == width - 1:
                print(box_parts["V"], end="")
            # Hor
            elif y == 0 or y == height - 1:
                print(box_parts["H"], end="")
            # Empty
            else:
                print(" ", end="")
        print()

# use function
draw_box(4,4, makeSquare=True)

# Cursor

# Cursor ANSI escape code
# Homework
# Make the box draw in the right place
# Allow coordinates so that they can draw inside of each other.