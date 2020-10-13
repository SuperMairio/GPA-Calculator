### GPA CALCULATOR BY MAIRI MACLEOD ###
#Designed for Abertay Uni's GPA system feel free to alter as you need x
gradeDict = {"A+":4.5, "A":4, "B+":3.5, "B":3, "C+":2.5, "C":2, "D+":1.5, "D":1, "MF":0.5} 

#Removes lowest x amount of grades (for covid weighting changes)
def RemoveLowest():
    howMany = int(input("How many grades can be removed? "))

    if len(currentGrades) == 12:
        currentGrades.sort()
    
        while howMany != 0:
            currentGrades.pop(0)
            howMany -= 1

#Calculates GPA with current grades and prints out the grade associated with it
def CalculateGPA(currentGrades):
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

    for i in howMany:
        grade = int(input("Please enter your grades one at a time\n pressing enter between each(Numbers not letters)"))
        currentGrades.append(grade)

    return(currentGrades)

def CalculateRequired(toRemove, numHave):
    toGet = int(input("How many modules do you have left? "))
    currentGrades = GetGrades(numHave)
    totalGrades = toGet + len(currentGrades)

    print("Calculating....")

    #This is some gross maths, I apologise
    a = currentGrades/totalGrades
    b = totalGrades - a


print("*** Mairi's GPA Calculator ***\n1: Calculate current GPA\n2: Calculate required grades\n3: Calculate potential GPA")
userInput = input("Please pick an option: ") 
howMany = int(input("How many grades do you currently have? "))

if (userInput == 1) | (userInput == 3):
    CalculateGPA(GetGrades(howMany))
elif userInput == 2:
    CalculateRequired(RemoveLowest(), howMany)
