a = int(input())
b = int(input())
c = int(input())

t = a + b + c

s = t%60
if s == 0:
    s = "00"
m = t//60
print(f"{m}:{s}")