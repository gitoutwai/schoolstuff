a = []
for _ in range(3):
    a.append(input())

b = []
for _ in range(3):
    b.append(input())

for c in a:
    for d in b:
        print(f"{c}{d} ", end="")