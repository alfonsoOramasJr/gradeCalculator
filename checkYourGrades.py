def setCourseName():
    print("Set the name of the course,")
    return input(">> ")

def setItemNames(courseName):
    itemNames = []

    print(f"Enter the items (homework, exams, etc) for {courseName}.")
    print("Enter nothing to quit entering items.")
    itemName = input('>> ')
    while itemName != '':
        itemNames.append(itemName)
        itemName = input('name: ')
    
    return itemNames

def setItemWeights(courseName, itemNames):
    itemWeights = []


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

main()