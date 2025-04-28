# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# 3/24/2025
# This has the class Intended Major to find out what major the student is aiming for

class intendedMajor():
    def __init__(self, intendedMajor):
        self.__intendedMajor = intendedMajor

    # Setter
    def setIntendedMajor(self, intendedMajor):
        self.__intendedMajor = intendedMajor

    # Getter
    def getIntendedMajor(self):
        return self.__intendedMajor

    # Str function
    def __str__(self):
        return self.__intendedMajor