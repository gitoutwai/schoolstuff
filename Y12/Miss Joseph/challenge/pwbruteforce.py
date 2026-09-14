code = int(input())

for x in range(65, 91):
    for y in range(65, 91):
        for z in range(65, 91):
            if x * y * z == code:
                print(chr(x)+chr(y)+chr(z))