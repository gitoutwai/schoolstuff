from random import randint

num = randint(1, 100)

guessed = False

while not guessed:
    u = int(input('num guess: '))

    if u > num:
        print("too high")
    elif u < num:
        print("too low")
    else:
        guessed = True