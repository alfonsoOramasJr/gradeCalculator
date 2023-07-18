def setCourseName():
    print("Set the name of the course,")
    return input(">> ")

def setCourseItems(courseName):
    itemCollection = []
    itemPair = []

    print(f"Enter the items (homework, exams, etc) for {courseName}.")
    print("Enter nothing to quit entering items.")
    itemName = input('>> ')
    itemPercentage = input('weight: ')
    while itemName != '':
        itemPair.append(itemName)
        itemPair.append(itemPercentage)
        itemName = input('name: ')
        itemPercentage = input('weight: ')
    
    return itemNames

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
    courseItems = setCourseItems(courseName)

main()