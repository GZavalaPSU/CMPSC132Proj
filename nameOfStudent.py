# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# 3/24/2025
# The program Name of Student gathers the full name of the student.

class nameOfStudent():
    def __init__(self, firstName, middleName, lastName):
        self.__firstName = firstName
        self.__middleName = middleName
        self.__lastName = lastName

    # Setters
    def setFirstName(self, firstName):
        self.__firstName = firstName
    def setMiddleName(self, middleName):
        self.__middleName = middleName
    def setLastName(self, lastName):
        self.__lastName = lastName

    # Getters
    def getFirstName(self):
        return self.__firstName
    def getMiddleName(self):
        return self.__middleName
    def getLastName(self):
        return self.__lastName

    # Str function
    def __str__(self):
        return (f"{self.__firstName} {self.__middleName} {self.__lastName}")