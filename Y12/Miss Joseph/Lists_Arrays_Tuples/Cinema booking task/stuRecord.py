class StuRecord:
    def __init__(self, first, last, dob, tutor):
        self.firstname = first
        self.surname = last
        self.dateOfBirth = dob
        self.tutorGroup = tutor

stu1 = StuRecord("Yeee", "Yoooo", "10/02/2010", "Boing 5")
stu2 = StuRecord("Heee", "Hoooo", "11/02/2011", "Ping 4")
stu3 = StuRecord("Feee", "Fiiii", "12/02/2012", "Foooo 3")

allRecords = []
allRecords.append(stu1)
allRecords.append(stu2)
allRecords.append(stu3)

print(allRecords)

print(allRecords[0].firstname)
print()

for i in range(len(allRecords)):
    print(allRecords[i].firstname)

with open("records.txt","w") as f:
    for i in range(len(allRecords)):
        data = f"{allRecords[i].firstname}, {allRecords[i].surname}, {allRecords[i].dateOfBirth}, {allRecords[i].tutorGroup}"
        f.write(data + "\n")