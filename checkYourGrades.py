def setCourseName():
    print("Set the name of the course,")
    return input(">> ")

## bug, since the loop doesn't end until the item name is appended we get an additional empty
## list item.
def setCourseItems(courseName):
    itemNames = []

    print(f"Enter the items (homework, exams, etc) for {courseName}.")
    print("Enter nothing to quit entering items.")
    itemName = input('>> ')
    while itemName != '':
        itemNames.append(itemName)
        itemName = input('>> ')
    
    return itemNames

def addCourseItem(courseName):
    pass

def removeCourseItem(courseName):
    pass

def findCourseItem(courseName):
    pass

def main():
    courseName = setCourseName()
    courseItems = setCourseItems(courseName)
    print(courseItems)

main()