text = input("text: ").lower()

final = ""

for char in text:
    if ord(char) > 96 and ord(char) < 124:
        final += char

rText = final[::-1]

if rText == final:
    print("Pally!")
else:
    print("No")