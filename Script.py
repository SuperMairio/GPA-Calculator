gradeDict = {"A+":4.5, "A":4, "B+":3.5, "B":3, "C+":2.5, "C":2, "D+":1.5, "D":1, "MF":0.5}

def RemoveLowest():
    howMany = int(input("How many grades can be removed? "))

    if len(currentGrades) == 12:
        currentGrades.sort()
    
        while howMany != 0:
            currentGrades.pop(0)
            howMany -= 1

def CalculateGPA(currentGrades):
    gpa = 0
    numberOfGrades = len(currentGrades)

    for grade in currentGrades:
        gpa += grade

    gpa = gpa/numberOfGrades
    
    print(gpa)

    for letter, value in gradeDict.items():
        if gpa >= value:


def GetGrades():
    currentGrades = []
    howmany = int(input("How many grades do you currently have? "))

    for i in howmany:
        grade = int(input("Please enter your grades one at a time\n pressing enter between each(Numbers not letters)"))
        currentGrades.append(grade)

    return(currentGrades)

def CalculateRequired(toRemove):


print("*** Mairi's GPA Calculator ***\n1: Calculate current GPA\n2: Calculate required grades")
userInput = input("Please pick an option: ") 

if userInput == 1:
    CalculateGPA(GetGrades())
if userInput == 2:
    CalculateRequired(RemoveLowest())