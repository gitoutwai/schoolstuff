StuNames = ["Bob","Lisa","Geo","Simi"] 
Subjects = ["Maths","English","CS"] 
 
#           Bob, Lisa, Geo, Simi 
AllScores = [[78, 54, 98, 63], #0 Maths 
             [99, 65, 79, 45], #1 English 
             [82, 67, 88, 59]] #2 CS

def display(StuNames, Subjects, AllScores):
    for s in range(len(StuNames)):
        print("Student:", StuNames[s])
        for q in range(len(AllScores)):
            print(f"{Subjects[q]}: {AllScores[q][s]}")

def average(StuNames, AllScores):
    for s in range(len(StuNames)):
        total = 0
        for q in range(len(AllScores)):
            total += AllScores[q][s]

        print(f"Average for {StuNames[s]}: {total/len(AllScores)}")

average(StuNames, AllScores)

class ScoreRecord:
    def __init__(self, name: str, MaScore: int, EnScore: int, CSScore: int):
        self.name = name
        self.Ma = MaScore
        self.En = EnScore
        self.Cs = CSScore

bob = ScoreRecord("Bob", 78, 99, 82)
lisa = ScoreRecord("Lisa", 54, 65, 67)
geo = ScoreRecord("Geo", 98, 79, 88)
simi = ScoreRecord("Simi", 63, 45, 59)

students = []
students.append(bob)
students.append(lisa)
students.append(geo)
students.append(simi)

totalMa = 0
totalEn = 0
totalCs = 0
for student in students:
    totalMa += student.Ma
    totalEn += student.En
    totalCs += student.Cs

print(totalMa/len(students))
print(totalEn/len(students))
print(totalCs/len(students))