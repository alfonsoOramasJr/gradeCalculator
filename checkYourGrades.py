def setCourseName():
    print("Set the name of the course,")
    return input(">> ")

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

    print(f"Enter the weights for each item (number value) under {courseName}")
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

def saveCourseToFile(courseName, courseItems):
    pass

def main():
    courseName = setCourseName()
    courseItems = setItemNames(courseName)
    courseWeights = setItemWeights(courseName, courseItems)

main()