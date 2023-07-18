def setCourseName():
    print("Set the name of the course,")
    courseName = input(">> ")
    return courseName

## So things like homework, classwork, exams, attendance, etc...
def setCourseItems(courseName):
    print("Enter the number amount of items (homework, exams, etc) for this course,")
    courseItems = input(">> ")
    courseItems = int(courseItems)

def addCourseItem(courseName):
    pass

def removeCourseItem(courseName):
    pass

def findCourseItem(courseName):
    pass

def main():
    courseName = setCourseName()

main()