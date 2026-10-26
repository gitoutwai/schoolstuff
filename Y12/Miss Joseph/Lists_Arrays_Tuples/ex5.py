metro = [["Airport", "Media City", "Tech Park", "City Centre", "University"], [4,2,1,3,0]]

start = int(input("Start station number: "))-1
end = int(input("End station number: "))-1

distance = 0

if start < 0 or start > 4 or end < 0 or end > 4:
    print("Invalid")
else:
    if start < end:
        for price in range(start, end):
            distance += metro[1][price]
    elif end < start:
        for price in range(start-1,end-1,-1):
            distance += metro[1][price]
    else:
        print("Invalid")

print(f"Price: ${distance*0.25}")