def setCourseName():
    print("Set the name of the course,")
    return input(">> ")

## So things like homework, classwork, exams, attendance, etc...
def setCourseItems(courseName):
    itemNames = []
    itemName = 'initial'

    print(f"Enter the items (homework, exams, etc) for {courseName}.")
    print("Enter nothing to quit entering items.")
    while itemName != '':
        itemName = input('>> ')
        itemNames.append(itemName)
    
    return itemNames

def addCourseItem(courseName):
    pass

def removeCourseItem(courseName):
    pass

def findCourseItem(courseName):
    pass

def main():
    courseName = setCourseName()

main()