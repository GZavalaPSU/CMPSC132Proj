# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# 3/24/2025
# This contains the ID of the student which is unique for each student

class studentIDNum:
    def __init__(self, studentID):
        self.__studentID = studentID

    # Setter
    def setStudentID(self, studentID):
        self.__studentID = studentID

    # Getter
    def getStudentID(self):
        return self.__studentID

    # Str function
    def __str__(self):
        return str(self.__studentID)