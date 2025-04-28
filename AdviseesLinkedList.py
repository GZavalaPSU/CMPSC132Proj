from AdviseeNode import AdviseeNode

class AdviseeLinkedList:
    def __init__(self):
        self.head = None

    def addAdvisee(self, student):
        newNode = AdviseeNode(student)
        newNode.next = self.head
        self.head = newNode

    def removeAdvisee(self, studentID):
        prev = None
        current = self.head
        while current:
            # Convert current student ID object to string for comparison
            if str(current.student.getID()) == str(studentID):
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True  # successfully removed
            prev = current
            current = current.next
        return False  # student not found

    def __str__(self):
        current = self.head
        result = ""
        while current:
            # Call student.name's __str__ method to get the full name
            result += f"Name: {current.student.getName()} | ID: {current.student.getID()}\n"
            current = current.next
        return result.strip()