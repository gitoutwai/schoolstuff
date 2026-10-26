from random import randint

sales = []
records = [[0,0,0,0,0],[100000,100000,100000,100000,100000]]

for y in range(4):
    sales.append([])
    for x in range(5):
        sales[y].append(randint(10000,90000))

print(sales)

for weekSales in sales:
    for shop in range(len(weekSales)):
        if weekSales[shop] > records[0][shop]:
            records[0][shop] = weekSales[shop]

        if weekSales[shop] < records[1][shop]:
            records[1][shop] = weekSales[shop]

print(records)