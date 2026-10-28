from random import randint

RNums = []

foundFlag = True

def linearSearch(userList, val):
    Found = False
    for index in range(0, len(userList)):
        if userList[index] == val:
            Found = True

    return Found

counter = 0

for _ in range(101):
    RNum = 0
    while linearSearch(RNums, RNum):
        RNum = randint(1,200)

    if RNum >= 66 and RNum <= 173:
        counter += 1
    RNums.append(RNum)

RNums.pop(0)
print(counter)
print(RNums)
print(len(RNums))