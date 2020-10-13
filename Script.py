### GPA CALCULATOR BY MAIRI MACLEOD ###
#Designed for Abertay Uni's GPA system feel free to alter as you need x
gradeDict = {"A+":4.5, "A":4, "B+":3.5, "B":3, "C+":2.5, "C":2, "D+":1.5, "D":1, "MF":0.5} 

#Removes lowest x amount of grades (for covid weighting changes)
def RemoveLowest(currentGrades):
    howMany = int(input("How many grades can be removed?\n(This assumes your lowest grades will already have been gotten) "))

    if len(currentGrades) == 12:
        currentGrades.sort()
    
        while howMany != 0:
            currentGrades.pop(0)
            howMany -= 1

    return(currentGrades)

#Calculates GPA with current grades and prints out the grade associated with it
def CalculateGPA(howMany):
    currentGrades = GetGrades(howMany)
    gpa = 0
    letterGrade = 0
    i = len(gradeDict)
    numberOfGrades = len(currentGrades)
    gradeList = list(gradeDict.keys())

    for grade in currentGrades:
        gpa += grade

    gpa = gpa/numberOfGrades

    #iterates through the dictionary and lets me access just the values
    for letter, value in gradeDict.items():
        if gpa >= value:
            letterGrade += 0.5
            i -= 1 
    
    print("Your current GPA: ("+gradeList[i]+")",gpa)

def GetGrades(howMany):
    currentGrades = []
    
    print("Make sure to enter your grades as numbers and press enter in between each one")

    while (len(currentGrades)) < howMany:
        grade = float(input("Please enter your grade: "))
        currentGrades.append(grade)

    return(currentGrades)

def CalculateRequired(numHave):
    toGet = int(input("How many modules do you have left? "))
    goal = float(input("What are you aiming for? (goal GPA) "))

    currentGrades = RemoveLowest(GetGrades(numHave))
    totalGrades = toGet + len(currentGrades)
    newGrades = []
    gradeList = list(gradeDict.keys())
    currentSum = 0
    x = 0

    print("Calculating....")

    #This is some gross maths, I apologise
    for grade in currentGrades:
        print(grade, currentGrades)
        currentSum += grade

    #add values to the array
    while x < toGet:
        newGrades.append(0)

    #if any grades are super low bump them to try and balance the grades
    #this works because if a grade is super low you must have at least one 4.5
    x = -1
    for score in newGrades:
        x += 1
        if score <= 2:
            newGrades[x] += 1
            try:
                highest = newGrades.index(4.5)
                newGrades[highest] -= 1
            except(ValueError):
                newGrades[x] -= 1

    print("Your required grades are:\n")

    for letterGrades in newGrades:
        print(gradeList[letterGrades]+":"+letterGrades)


print("******************************\n*** Mairi's GPA Calculator ***\n******************************\n1: Calculate current GPA\n2: Calculate required grades\n3: Calculate potential GPA")
userInput = input("\nPlease pick an option: ") 

if (userInput == "1") | (userInput == "3"):
    howMany = int(input("How many grades do you currently have? "))
    CalculateGPA(howMany)
elif userInput == "2":
    howMany = int(input("How many grades do you currently have? "))
    CalculateRequired(howMany)
else:
    exit()