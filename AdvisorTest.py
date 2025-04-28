from nameOfStudent import nameOfStudent
from studentIDNum import studentIDNum
from MailingAddress import Address
from email import email
from phoneNumber import phoneNumber
from Date import Date
from intendedMajor import intendedMajor
from Student import Student
from Advisor import Advisor
from Course import Course
from AdviseesLinkedList import AdviseeLinkedList
from AdvisorMenu import AdvisorMenu

# Helper function to create a student with 3 courses
def createStudent(first, middle, last, idNum, majorName, courseData):
    name = nameOfStudent(first, middle, last)
    sid = studentIDNum(idNum)
    address = Address("123", "College Ave", "State College", "PA", "16801", "Home")
    emails = [email(f"{first.lower()}@email.com", "Personal")]
    phones = [phoneNumber("814-123-4567", "Personal")]
    birth = Date("01", "01", "2000")
    accepted = Date("06", "01", "2024")
    start = Date("08", "26", "2024")
    major = intendedMajor(majorName)

    student = Student(name, sid, address, emails, phones, birth, accepted, start, major)

    # Add 3 courses from courseData
    for cd in courseData:
        course = Course(cd["num"], cd["sem"], cd["delivery"], cd["status"], cd["grade"])
        student.addCourse(course)

    return student

# Create students with 3 courses each
student1 = createStudent(
    "Alice", "M", "Johnson", "1111111111", "Computer Science",
    [
        {"num": "CMPSC 132", "sem": "Fall 2024", "delivery": "in-person", "status": "completed", "grade": "A"},
        {"num": "MATH 140", "sem": "Fall 2024", "delivery": "hybrid", "status": "completed", "grade": "B"},
        {"num": "ENGL 15", "sem": "Fall 2024", "delivery": "remote", "status": "completed", "grade": "A"},
    ]
)

student2 = createStudent(
    "Brian", "", "Lee", "2222222222", "Biology",
    [
        {"num": "BIOL 110", "sem": "Fall 2024", "delivery": "in-person", "status": "on-going", "grade": "N/A"},
        {"num": "CHEM 110", "sem": "Fall 2024", "delivery": "in-person", "status": "on-going", "grade": "N/A"},
        {"num": "STAT 200", "sem": "Fall 2024", "delivery": "remote", "status": "on-going", "grade": "N/A"},
    ]
)

student3 = createStudent(
    "Clara", "L", "Nguyen", "3333333333", "Psychology",
    [
        {"num": "PSYCH 100", "sem": "Fall 2024", "delivery": "in-person", "status": "completed", "grade": "A"},
        {"num": "SOC 001", "sem": "Fall 2024", "delivery": "hybrid", "status": "completed", "grade": "A"},
        {"num": "HDFS 129", "sem": "Fall 2024", "delivery": "remote", "status": "completed", "grade": "B"},
    ]
)

# List of all students
allStudents = [student1, student2, student3]

# Create advisor and assign students
advisor = Advisor("Gregory", "Smith", "", "Professor", "Computer Science")
advisor.addAdvisee(student1)
advisor.addAdvisee(student2)
advisor.addAdvisee(student3)

# Launch menu
AdvisorMenu(allStudents + [student1, student2, student3])
