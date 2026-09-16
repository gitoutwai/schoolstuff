text = input("String: ")
key = int(input("Enter shift(- for left, + for right): "))
key = key % 26

newString = ""
for chara in range(len(text)):
    character = text[chara]
    Val = ord(character)

    if Val >= 65 and Val <= 90:
        Val += key
        if 65 > Val:
            Val += 26
        elif Val > 90:
            val -= 26
    elif Val >= 97 and Val <= 122:
        Val += key
        if 97 > Val:
            Val += 26
        elif Val > 122:
            Val -= 26

    newString += chr(Val)

print(newString)