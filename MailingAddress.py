# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# 3/24/2025
# This program has the class Address to gather the information to fill out where the student lives

class Address():
    def __init__(self, streetNumber, street,  city, state,  zipCode, typeOfHouse):
        self.__streetNumber = streetNumber
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipCode = zipCode
        self.__typeOfHouse = typeOfHouse

    # Setters
    def setstreetNumber(self, streetNumber):
        self.__streetNumber = streetNumber
    def setStreet(self, street):
        self.__street = street
    def setCity(self, city):
        self.__city = city
    def setState(self, state):
        self.__state = state
    def setZipCode(self, zipCode):
        self.__zipCode = zipCode
    def setTypeOfHouse(self, typeOfHouse):
        self.__typeOfHouse = typeOfHouse

    # Getters
    def getstreetNumber(self):
        return self.__streetNumber
    def getStreet(self):
        return self.__street
    def getCity(self):
        return self.__city
    def getState(self):
        return self.__state
    def getZipCode(self):
        return self.__zipCode
    def getTypeOfHouse(self):
        return self.__typeOfHouse

    # Str function
    def __str__(self):
        return f"{self.__streetNumber} {self.__street}, {self.__city}, {self.__state}, {self.__zipCode}. {self.__typeOfHouse}"