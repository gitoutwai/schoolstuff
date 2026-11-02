from random import choice

# Init

Attend = []
for i in range(7):
    Attend.append([])
    for z in range(6):
        if i == 0:
            Attend[i].append(z+1)

for i in range(1,7):
    for z in range(6):
        if i == 6:
            Attend[i].append(0)
        else:
            Attend[i].append(choice([True, False]))

print(Attend)

for i in range(1,6):
    for z in range(6):
        if Attend[i][z] == False:
            Attend[6]