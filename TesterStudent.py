# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# CMPSC 132
# 3/24/2025
# This program uses 5 example students to demonstrate the functionality of the Academic Advisor Program

# Email and Phone should be a list.
    # Add, edit, remove email + Phone


from Student import Student
from nameOfStudent import nameOfStudent
from studentIDNum import studentIDNum
from MailingAddress import Address
from email import email
from phoneNumber import phoneNumber
from Date import Date
from intendedMajor import intendedMajor
from menu import menu
from AdvisorMenu import AdvisorMenu
from Course import Course
from Advisor import Advisor

listOfStudents = []

# Fills out example of student info
studentName = nameOfStudent("Brandon", "Alexander", "Bula")
studentID = studentIDNum("1234567890")
studentAddress = Address("91", "Rabbit Run Road",  "Parkesburg", "PA",  "19365", "Home")
studentEmail = [email("helloworld@gmail.com", "Personal")]
studentPhoneNumber = [phoneNumber("484-123-0987", "Work")]
studentBirthDate = Date("04", "12", "2006")
studentAcceptedDate = Date("06", "12", "2024")
studentSemesterStart = Date("08", "30", "2024")
studentIntendedMajor = intendedMajor("Computer Science")

# Appends student info
student = Student(studentName, studentID, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
student.addCourse(Course("CS101", "Fall 2024", "In-person", "Completed", "A"))
student.addCourse(Course("CS201", "Spring 2025", "Online", "In Progress", "N/A"))
student.addCourse(Course("CS310", "Fall 2025", "In-person", "Not Started", "N/A"))
listOfStudents.append(student)

studentName = nameOfStudent("John", "B", "Doe")
studentID = studentIDNum("7203650189")
studentAddress = Address("123", "Baker Street", "Downingtown", "DE", "19335", "Apartment")
studentEmail = [email("tester@hotmail.com", "Work")]
studentPhoneNumber = [phoneNumber("610-789-1234", "Personal")]
studentBirthDate = Date("01", "02", "2000")
studentAcceptedDate = Date("06", "12", "2024")
studentSemesterStart = Date("08", "30", "2024")
studentIntendedMajor = intendedMajor("Computer Science")

student = Student(studentName, studentID, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
student.addCourse(Course("CS102", "Fall 2024", "In-person", "Completed", "B+"))
student.addCourse(Course("CS250", "Spring 2025", "Hybrid", "In Progress", "N/A"))
student.addCourse(Course("CS355", "Fall 2025", "Online", "Not Started", "N/A"))
listOfStudents.append(student)

studentName = nameOfStudent("Mac", "C", "Conor")
studentID = studentIDNum("8759350958")
studentAddress = Address("986", "Summer Lane", "Fore", "CA", "18753", "House")
studentEmail = email("tester@yahoo.com", "Work")
studentPhoneNumber = phoneNumber("123-456-7891", "Personal")
studentBirthDate = Date("01", "02", "2000")
studentAcceptedDate = Date("06", "12", "2024")
studentSemesterStart = Date("08", "30", "2024")
studentIntendedMajor = intendedMajor("Biology")
student.addCourse(Course("POL101", "Fall 2024", "Online", "Completed", "A"))
student.addCourse(Course("POL210", "Spring 2025", "Hybrid", "In Progress", "N/A"))
student.addCourse(Course("POL303", "Fall 2025", "In-person", "Not Started", "N/A"))
student = Student(studentName, studentID, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
student.addCourse(Course("BIO101", "Fall 2024", "In-person", "Completed", "A-"))
student.addCourse(Course("BIO220", "Spring 2025", "Online", "In Progress", "N/A"))
student.addCourse(Course("BIO330", "Fall 2025", "In-person", "Not Started", "N/A"))
listOfStudents.append(student)

studentName = nameOfStudent("Charles", "Q", "Pop")
studentID = studentIDNum("6329103729")
studentAddress = Address("524", "Runner Street", "Broke", "DE", "19335", "Apartment")
studentEmail = [email("bingbong@gmail.com", "Work")]
studentPhoneNumber = [phoneNumber("867-193-7489", "Personal")]
studentBirthDate = Date("01", "02", "2000")
studentAcceptedDate = Date("06", "12", "2024")
studentSemesterStart = Date("08", "30", "2024")
studentIntendedMajor = intendedMajor("Political Science")

student = Student(studentName, studentID, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
student.addCourse(Course("POL101", "Fall 2024", "Online", "Completed", "A"))
student.addCourse(Course("POL210", "Spring 2025", "Hybrid", "In Progress", "N/A"))
student.addCourse(Course("POL303", "Fall 2025", "In-person", "Not Started", "N/A"))
listOfStudents.append(student)

studentName = nameOfStudent("Dom", "B", "Sinclear")
studentID = studentIDNum("2470836766")
studentAddress = Address("757", "Rabbit Run Road", "Getty", "DE", "83024", "Apartment")
studentEmail = [email("tester@hotmail.com", "Work"), email("woker@gmail.com","Personal")]
studentPhoneNumber = [phoneNumber("610-789-1234", "Personal")]
studentBirthDate = Date("01", "02", "2000")
studentAcceptedDate = Date("06", "12", "2024")
studentSemesterStart = Date("08", "30", "2024")
studentIntendedMajor = intendedMajor("Computer Science")

student = Student(studentName, studentID, studentAddress, studentEmail, studentPhoneNumber, studentBirthDate, studentAcceptedDate, studentSemesterStart, studentIntendedMajor)
student.addCourse(Course("CS102", "Fall 2024", "In-person", "Completed", "A"))
student.addCourse(Course("CS103", "Spring 2025", "In-person", "In Progress", "N/A"))
student.addCourse(Course("CS420", "Fall 2025", "In-person", "Not Started", "N/A"))
listOfStudents.append(student)

advisor = Advisor("Dr.", "Emily", "Clark", "Professor", "Computer Science")

# Add advisees to the advisor (select 3 students from the list)
for student in listOfStudents:
    if student.ID.getStudentID() in ["1234567890", "7203650189", "2470836766"]:  # Matching Student IDs
        advisor.addAdvisee(student)

if __name__ == "__main__":
    while True:
        user = int(input("\nAre modifying a\n"
                         "1. Student\n"
                         "2. Advisor\n"
                         "3. Quit\n"))
        if user == 1:
            menu(listOfStudents)
        elif user == 2:
            AdvisorMenu(listOfStudents)
        elif user == 3:
            break
