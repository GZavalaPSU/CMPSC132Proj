from CourseNode import CourseNode

class CourseLinkedList:
    def __init__(self):
        self.head = None

    def addCourse(self, course):
        newNode = CourseNode(course)
        newNode.next = self.head
        self.head = newNode

    def removeCourse(self, courseNumber):
        prev = None
        current = self.head
        while current:
            if current.course.getCourseNumber() == courseNumber:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True  # successfully removed
            prev = current
            current = current.next
        return False  # course not found

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.course) + "\n"
            current = current.next
        return result.strip()
