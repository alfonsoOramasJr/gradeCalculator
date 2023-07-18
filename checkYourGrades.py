def setCourseName():
    print("Set the name of the course,")
    return input("name: ")

def setItemNames(courseName):
    itemNames = []

    print(f"Enter the items (homework, exams, etc) for {courseName}.")
    print("Enter nothing to quit entering items.")
    itemName = input('name: ')
    while itemName != '':
        itemNames.append(itemName)
        itemName = input('name: ')
    
    return itemNames

def setItemWeights(courseName, itemNames):
    itemWeights = []

    print(f"Enter the percentage amount for how much each item under {courseName} is worth")
    for item in itemNames:
        itemWeight = input(f"{item}'s weight is: ")
        itemWeights.append(itemWeight)
    
    return itemWeights

def addCourseItem(courseName):
    pass

def removeCourseItem(courseName):
    pass

def findCourseItem(courseName):
    pass

def saveCourseToFile(courseName, courseItems, courseWeights):
    courseFile = open('courses.txt', 'a')
    
    courseFile.close()

def main():
    courseName = setCourseName()
    courseItems = setItemNames(courseName)
    courseWeights = setItemWeights(courseName, courseItems)

main()