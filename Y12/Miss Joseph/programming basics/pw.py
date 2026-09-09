pw = input('pw ')

yes = True
upper = False
lower = False
num = False
if len(pw) >= 8:
    for char in pw:
        code = ord(char)

        if code >= 65 and code <= 90:
            upper = True
        elif code >= 97 and code <= 122:
            lower = True
        elif code >= 48 and code <= 57:
            num = True

    if not(num and lower and upper):
        yes = False
else:
    yes = False

if yes:
    print('strong')
else:
    print('weak')