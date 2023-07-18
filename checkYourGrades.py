def setCourseName():
    print("Set the name of the course,")
    return input(">> ")

## So things like homework, classwork, exams, attendance, etc...
def setCourseItems(courseName):
    print(f"Enter the number amount of items (homework, exams, etc) for {courseName},")
    courseItems = input(">> ")
    courseItems = int(courseItems)

    itemNames = []
    for iterator in range(len(courseItems)):
        itemNames.append(input(f"({iterator}) Enter the name of the course item"))
    
    return itemNames

def addCourseItem(courseName):
    pass

def removeCourseItem(courseName):
    pass

def findCourseItem(courseName):
    pass

def main():
    courseName = setCourseName()
    print(courseName)

main()