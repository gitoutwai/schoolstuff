text = input()
key = input().lower()

i = 0
newString = ""
for charIndex in range(len(text)):
    advance = False
    keyIndex = ord(key[i])-97
    chara = text[charIndex]
    val = ord(chara)

    if val >= 65 and val <= 90:
        val += keyIndex
        if 65 > val:
            val += 26
        elif val > 90:
            val -= 26

        advance = True
    elif val >= 97 and val <= 122:
        val += keyIndex
        if 97 > val:
            val += 26
        elif val > 122:
            val -= 26

        advance = True

    if advance:
        newString += chr(val)
        i += 1
        if i > len(key)-1:
            i = 0

print(newString)