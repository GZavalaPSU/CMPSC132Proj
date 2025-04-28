# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# 3/24/2025
# This has the class Student to gather all the information regarding the student
# from name, ID, address, email, phone number, birthdate, acceptance date, start of semester, and intended Major

from CourseLinkedList import CourseLinkedList

class Student():
    def __init__(self, name, ID, address, email, phone, birthdate, acceptanceDate, semesterStart, intededMajor):
        self.name = name
        self.ID = ID
        self.address = address
        self.email = email
        self.phone = phone
        self.birthdate = birthdate
        self.acceptanceDate = acceptanceDate
        self.semesterStart = semesterStart
        self.intendedMajor = intededMajor

        self.__courseList = CourseLinkedList()

    # Setters
    def setName(self, name):
        self.name = name
    def setID(self, ID):
        self.ID = ID
    def setAddress(self, address):
        self.address = address
    def setEmail(self, email):
        self.email = email
    def setPhone(self, phone):
        self.phone = phone
    def setBirthdate(self, birthdate):
        self.birthdate = birthdate
    def setAcceptanceDate(self, acceptanceDate):
        self.acceptanceDate = acceptanceDate
    def setSemesterStart(self, semesterStart):
        self.semesterStart = semesterStart
    def setIntededMajor(self, intededMajor):
        self.intendedMajor = intededMajor

    # Getters
    def getName(self):
        return self.name
    def getID(self):
        return self.ID
    def getAddress(self):
        return self.address
    def getEmail(self):
        return self.email
    def getPhone(self):
        return self.phone
    def getBirthdate(self):
        return self.birthdate
    def getAcceptanceDate(self):
        return self.acceptanceDate
    def getSemesterStart(self):
        return self.semesterStart
    def getIntededMajor(self):
        return self.intendedMajor

    def getCourseList(self):
        return self.__courseList

    def addCourse(self, course):
        self.__courseList.addCourse(course)
    def removeCourse(self, courseNumber):
        return self.__courseList.removeCourse(courseNumber)



    def studentInfo(self):
        print(f"Student Name: {self.name}\n"
                f"Student ID: {self.ID}\n"
                f"Student Address: {self.address}\n"
              ,end="")
        for i in self.email:
            print(f"Student Email: {i}\n", end="")
        for i in self.phone:
            print(f"Student Phone: {i}\n",end="")
        print(
            f"Student Birthdate: {self.birthdate}\n"
            f"Student Acceptance Date: {self.acceptanceDate}\n"
            f"Student Semester Start Date: {self.semesterStart}\n"
            f"Student Intended Major: {self.intendedMajor}\n")