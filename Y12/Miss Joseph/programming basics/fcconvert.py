choice = input("inputted temp (c)elsius or (f)ahrenheit? ").lower()

temp = int(input("temp: "))

if choice == "c":
    print(f"temp in f: {temp*1.8 + 32}")
elif choice == "f":
    print(f"temp in c: {(temp-32) / 1.8}")