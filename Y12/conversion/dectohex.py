def method1():
    num = int(input())

    print(hex(num).removeprefix("0x"))

def method2():
    valueConvert = {
        10:"A",
        11:"B",
        12:"C",
        13:"D",
        14:"E",
        15:"F"
    }

    num = int(input())
    i = 0
    while num // (16**i) != 0:
        i += 1
        print("y")

    final = ""
    while num != 0:
        val = num % (16**i)
        if val >= 10:
            val = valueConvert[val]
        final += str(val)
        num -= num % (16**i)
        i -= 1

    print(final)

method2()