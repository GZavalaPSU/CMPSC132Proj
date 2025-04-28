from AdviseesLinkedList import AdviseeLinkedList

class Advisor:
    def __init__(self, firstName, lastName, middleName, title, department):
        self.__firstName = firstName
        self.__middleName = middleName
        self.__lastName = lastName
        self.__title = title
        self.__department = department
        self.__adviseeList = AdviseeLinkedList()

    # Getters
    def getFirstName(self):
        return self.__firstName
    def getMiddleName(self):
        return self.__middleName
    def getLastName(self):
        return self.__lastName
    def getTitle(self):
        return self.__title
    def getDepartment(self):
        return self.__department
    def getAdviseeList(self):
        return self.__adviseeList

    # Setters
    def setFirstName(self, firstName):
        self.__firstName = firstName
    def setMiddleName(self, middleName):
        self.__middleName = middleName
    def setLastName(self, lastName):
        self.__lastName = lastName
    def setTitle(self, title):
        self.__title = title
    def setDepartment(self, department):
        self.__department = department

    # Methods to edit advisee list
    def addAdvisee(self, student):
        self.__adviseeList.addAdvisee(student)

    def removeAdvisee(self, studentID):
        return self.__adviseeList.removeAdvisee(studentID)

    def __str__(self):
        fullName = f"{self.__firstName} {self.__middleName} {self.__lastName}"
        return (f"Advisor Name: {fullName}\n"
            f"Title: {self.__title}\n"
            f"Department: {self.__department}\n"
            f"Advisees:\n{str(self.__adviseeList) if str(self.__adviseeList).strip() else 'No advisees yet.'}")
