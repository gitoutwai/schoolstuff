def main():
    balance = 200
    uw = int(input("Want money?\n"))
    if uw > 0 and uw <= balance:
        balance -= uw
        print("Money gone!")
    else:
        print("No money for u womp womp :(")

main()