class Course:
    def __init__(self, courseNumber, semesterTaken, deliveryMethod, status, grade):
        self.__courseNumber = courseNumber
        self.__semesterTaken = semesterTaken
        self.__deliveryMethod = deliveryMethod
        self.__status = status
        self.__grade = grade

    # Setters
    def setCourseNumber(self, courseNumber):
        self.__courseNumber = courseNumber
    def setSemesterTaken(self, semesterTaken):
        self.__semesterTaken = semesterTaken
    def setDeliveryMethod(self, deliveryMethod):
        self.__deliveryMethod = deliveryMethod
    def setStatus(self, status):
        self.__status = status
    def setGrade(self, grade):
        self.__grade = grade

    # Getters
    def getCourseNumber(self):
        return self.__courseNumber
    def getSemesterTaken(self):
        return self.__semesterTaken
    def getDeliveryMethod(self):
        return self.__deliveryMethod
    def getStatus(self):
        return self.__status
    def getGrade(self):
        return self.__grade

    # Custom string representation
    def __str__(self):
        return (
            f"Course: {self.__courseNumber}, Semester: {self.__semesterTaken}, "
            f"Delivery: {self.__deliveryMethod}, Status: {self.__status}, Grade: {self.__grade}"
        )
