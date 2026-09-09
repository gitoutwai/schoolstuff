days = 0

for _ in range(30):
    if input("Here? ").lower() == "y":
        days += 1
    elif input("Here? ").lower() == "n":
        pass

print(f"{days}/30")