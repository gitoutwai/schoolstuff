array = [[],[],[],[],[],[]]

def initArray(array):
    for y in array:
        for _ in range(5):
            y.append("-")

def resetArray(array):
    for y in array:
        for x in array:
            x = "-"

def displayArray(array):
    print("_"*len(array[0]) * 2)
    for y in array:
        print("|")
        for x in array:
            print(x, "|", end="")
        print()
    print("-"*len(array[0]) * 2)

initArray(array)

displayArray(array)