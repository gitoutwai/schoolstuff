try:
    num1 = float(input('num1: '))
    num2 = float(input('num2: '))
    op = input("operator: ")

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("bruh")

except ValueError:
    print("I am not subtracting strings for u :/")