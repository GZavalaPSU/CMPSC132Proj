# CMPSC132
# Gabriel Zavala Alonso and Brandon Bula
# 3/5/2025
# This program prompts the user with options on what to do with a student's info. This includes creating a Student, editing a student, deleting a student, and displaying a Student.

from Student import Student
from nameOfStudent import nameOfStudent
from studentIDNum import studentIDNum
from MailingAddress import Address
from email import email
from phoneNumber import phoneNumber
from Date import Date
from intendedMajor import intendedMajor
from Course import Course

def menu(listOfStudents):
    print("Welcome to our Academic Advisor Management program to be \nable to quickly edit students information!")
    while True:
        # Gathers input to decide what option to perform on the student
        userInput = input("\nWhat would you like to do?\n"
                          "1. Create a Student\n"
                          "2. Edit a Student\n"
                          "3. Delete a Student\n"
                          "4. Display a Student\n"
                          "5. Quit\n")

        # Creates a student and adds it to the list
        if userInput == "1":
            while True:
                # Name
                firstName = input("\nFirst Name: ")
                middleName = input("Middle Name: ")
                lastName = input("Last Name: ")
                studentName = nameOfStudent(firstName, middleName, lastName)
    
                # Student ID
                while True:
                    try:
                        studentID = input("\nStudent ID: ")
                        for w in listOfStudents:
                            if w.ID == studentID:
                                raise ValueError("This Student ID is already taken.")
                        else:
                            studentIDNumber = studentIDNum(studentID)
                        break
                    except ValueError:
                        print("Please enter a valid student ID (Already taken).")
    
                # Address
                streetNumber = input("\nStreet Number: ")
                street = input("Street: ")
                city = input("City: ")
                state = input("State: ")
                zipCode = input("Zip Code: ")
                typeOfHouse = input("Type of House: ")
                studentAddress = Address(streetNumber, street, city, state, zipCode, typeOfHouse)
    
                # Email
                emailAddress = input("\nEmail: ")
                emailType = input("Email Type: ")
                studentEmails = [email(emailAddress, emailType)]
    
                # Phone Number
                number = input("\nPhone Number: ")
                numberType = input("Phone Type: ")
                studentPhoneNumber = [phoneNumber(number, numberType)]
    
                # Date Born
                monthBorn = input("\nMonth Born: ")
                dayBorn = input("Day Born: ")
                yearBorn = input("Year Born: ")
                birthday = Date(monthBorn, dayBorn, yearBorn)
    
                # Date Accepted
                monthAccepted = input("\nMonth Accepted: ")
                dayAccepted = input("Day Accepted: ")
                yearAccepted = input("Year Accepted: ")
                acceptanceDate = Date(monthAccepted, dayAccepted, yearAccepted)
    
                # Semester Start Date
                monthSemesterStart = input("\nMonth Semester Start: ")
                daySemesterStart = input("Day Semester Start: ")
                yearSemesterStart = input("Year Semester Start: ")
                semesterStart = Date(monthSemesterStart, daySemesterStart, yearSemesterStart)
    
                # Intended Major Picked
                intendedMajorPicked = input("\nIntended Major: ")
                StudentIntendedMajor = intendedMajor(intendedMajorPicked)

                # Adding Courses
                courses = []  # Temporary list to store courses
                while True:
                    addCourse = input("Would you like to add a course for this student? (Y/N): ")
                    if addCourse.lower() == "y":
                        courseNumber = input("Course Number: ")
                        semesterTaken = input("Semester Taken: ")
                        deliveryMethod = input("Delivery Method (Online/In-person): ")
                        status = input("Status (Completed/In Progress): ")
                        grade = input("Grade (if applicable): ")

                        newCourse = Course(courseNumber, semesterTaken, deliveryMethod, status, grade)
                        courses.append(newCourse)  # Add course to temporary list
                        print("Course added successfully.")
                    else:
                        break

                studentInfo = Student(
                    studentName, studentIDNumber, studentAddress, studentEmails,
                    studentPhoneNumber, birthday, acceptanceDate, semesterStart,
                    StudentIntendedMajor
                )
                listOfStudents.append(studentInfo)

                # Add courses to student's course list
                for course in courses:
                    studentInfo.addCourse(course)

                print(f"You finished creating {studentName}, {studentIDNumber}!")

                continued = input("Would you like to make another student? (Y/N)\n")
                if continued == "Y":
                    continue
                else:
                    break


        # Edit a Student
        elif userInput == "2":
            if len(listOfStudents) == 0:
                print("\nYou have not created any students to edit.\n")
                continue
            while True:
                # Determine what student to edit
                print("\nHere is a list of students name and ID:")
                for i in listOfStudents:
                    print(f"{i.name}\n{i.ID}\n")
                studentIDSelected = input("Student ID You Would Like to Edit: ")

                # Menu to see what gets edited
                for edited in listOfStudents:
                    if edited.ID.getStudentID() == studentIDSelected:
                        while True:
                            userInputToChange = input("\nWhat would you like to change?\n"
                                                      "1. Name\n"
                                                      "2. ID\n"
                                                      "3. Address\n"
                                                      "4. Email\n"
                                                      "5. Phone Number\n"
                                                      "6. Birthdate\n"
                                                      "7. Acceptance Date\n"
                                                      "8. Semester Start\n"
                                                      "9. Intended Major\n"
                                                      "10. Add Courses\n"
                                                      "11. Remove Courses\n"
                                                      f"12. Quit Editing {edited.getID()}\n")

                            # Name
                            if userInputToChange == "1":
                                firstName = input("First Name: ")
                                middleName = input("Middle Name: ")
                                lastName = input("Last Name: ")
                                edited.name = nameOfStudent(firstName, middleName, lastName)

                            # Student ID
                            elif userInputToChange == "2":
                                while True:
                                    try:
                                        studentID = input("Student ID: ")
                                        for possibleStudent in listOfStudents:
                                            if possibleStudent.ID.getStudentID() == studentID:
                                                print("This Student ID is already taken.")
                                                raise ValueError()
                                        else:
                                            edited.ID=studentIDNum(studentID)
                                        break
                                    except ValueError:
                                        print("Invalid input. Please enter a valid ID.")

                            # Street Number
                            elif userInputToChange == "3":
                                streetNumber = input("Street Number: ")
                                street = input("Street: ")
                                city = input("City: ")
                                state = input("State: ")
                                zipCode = input("Zip Code: ")
                                typeOfHouse = input("Type of House: ")
                                edited.address = Address(streetNumber, street, city, state, zipCode, typeOfHouse)

                            # Email
                            elif userInputToChange == "4":
                                while True:
                                    emailInput = input("What would you like to do with the email?\n"
                                                       "1. Add email\n"
                                                       "2. Change email\n"
                                                       "3. Remove email\n"
                                                       "4. Exit\n")
                                    if emailInput == "1":
                                        emailAddress = input("Email: ")
                                        emailType = input("Email Type: ")
                                        edited.email.append(email(emailAddress, emailType))
                                    elif emailInput == "2":
                                        if not edited.email:
                                            print("No emails to change.")
                                            continue
                                        for i in range(len(edited.email)):
                                            print(f"{i + 1}. {edited.email[i].getEmail()}")
                                        try:
                                            index = int(input("Select email number to change: ")) - 1
                                            newEmail = input("New Email: ")
                                            newType = input("New Email Type: ")
                                            edited.email[index] = (email(newEmail, newType))
                                        except (ValueError, IndexError):
                                            print("Invalid selection.")

                                    elif emailInput == "3":
                                        if not edited.email:
                                            print("No email to remove.")
                                            continue
                                        for i in range(len(edited.email)):
                                            print(f"{i + 1}. {edited.email[i].getEmail()}")
                                        try:
                                            index = int(input("Select email number to remove: ")) - 1
                                            removed = edited.email.pop(index)
                                            print(f"Removed {removed.getEmail()}")
                                        except (ValueError, IndexError):
                                            print("Invalid selection.")

                                    elif emailInput == "4":
                                        break


                            # Phone Number
                            elif userInputToChange == "5":
                                while True:
                                    numberInput = input("What would you like to do with the Phone Number?\n"
                                                       "1. Add number\n"
                                                       "2. Change number\n"
                                                       "3. Remove number\n"
                                                       "4. Exit\n")
                                    if numberInput == "1":
                                        number = input("Phone Number: ")
                                        numberType = input("Phone Type: ")
                                        edited.phone = [phoneNumber(number, numberType)]

                                    elif numberInput == "2":
                                        if not edited.phone:
                                            print("No phone number to change.")
                                            continue
                                        for i in range(len(edited.phone)):
                                            print(f"{i + 1}. {edited.phone[i].getNumber()}")
                                        try:
                                            index = int(input("Select phone number to change: ")) - 1
                                            newNumber = input("New Phone Number: ")
                                            newType = input("New Phone Type: ")
                                            edited.phone[index] = (email(newNumber, newType))
                                        except (ValueError, IndexError):
                                            print("Invalid selection.")

                                    elif numberInput == "3":
                                        if not edited.phone:
                                            print("No phone number to remove.")
                                            continue
                                        for i in range(len(edited.phone)):
                                            print(f"{i + 1}. {edited.phone[i].getNumber()}")
                                        try:
                                            index = int(input("Select phone number to remove: ")) - 1
                                            removed = edited.phone.pop(index)
                                            print(f"Removed {removed.getNumber()}")
                                        except (ValueError, IndexError):
                                            print("Invalid selection.")

                                    elif numberInput == "4":
                                        break


                            # Birth Date
                            elif userInputToChange == "6":
                                month = input("Month: ")
                                day = input("Day: ")
                                year = input("Year: ")
                                edited.birthdate = Date(month, day, year)

                            # Acceptance Date
                            elif userInputToChange == "7":
                                month = input("Month: ")
                                day = input("Day: ")
                                year = input("Year: ")
                                edited.acceptanceDate = Date(month, day, year)

                            # Semester Start
                            elif userInputToChange == "8":
                                month = input("Month: ")
                                day = input("Day: ")
                                year = input("Year: ")
                                edited.semesterStart = Date(month, day, year)

                            # Intended Major Picked
                            elif userInputToChange == "9":
                                intendedMajorPicked = input("Intended Major: ")
                                edited.intendedMajor = intendedMajor(intendedMajorPicked)

                            # Course Management
                            elif userInputToChange == "10":  # Adding Courses
                                while True:
                                    courseNumber = input("Enter course number: ")
                                    semesterTaken = input("Enter semester taken: ")
                                    deliveryMethod = input("Enter delivery method (Online/In-person): ")
                                    status = input("Enter status (Completed/In Progress): ")
                                    grade = input("Enter grade (if applicable): ")

                                    newCourse = Course(courseNumber, semesterTaken, deliveryMethod, status, grade)
                                    edited.addCourse(newCourse)
                                    print("Course added successfully.")

                                    end = input("Would you like to add another course? (Y/N): ")
                                    if end.lower() == "n":
                                        break

                            elif userInputToChange == "11":  # Removing Courses
                                while True:
                                    if not edited.getCourseList():  # Check if student has any courses
                                        print("No courses to remove.")
                                        break

                                    print("\n--- Current Courses ---")
                                    print(edited.getCourseList())  # Display courses
                                    courseToRemove = input("Enter course number to remove: ")

                                    if edited.removeCourse(courseToRemove):
                                        print(f"Course {courseToRemove} removed successfully.")
                                    else:
                                        print("Course not found.")

                                    end = input("Would you like to remove another course? (Y/N): ")
                                    if end.lower() == "n":
                                        break

                            elif userInputToChange == "12":
                                break
                        else:
                            print("Not a valid choice!")
                end = input("\nWould you like edit another student? (Y/N)\n")
                if end == "Y":
                    continue
                else:
                    break


        # Delete a Student
        elif userInput == "3":
            while True:
                for i in listOfStudents:
                    print(f"{i.name}\n{i.ID}\n")
                studentToDelete = input("Enter Student ID of Student to Delete: ")

                for student in listOfStudents:
                    if student.ID.getStudentID() == studentToDelete:
                        print(student.studentInfo())
                        confirmDelete = input(f"Delete {student.name} {student.ID.getStudentID()}? (Y/N): ")
                        if confirmDelete == "Y":
                            listOfStudents.remove(student)
                            print(f"Student {student.name} (ID: {student.ID}) has been deleted.")
                        break
                end = input("\nWould you like to delete another student? (Y/N)\n")
                if end == "Y":
                    continue
                else:
                    break


        # View a Student
        elif userInput == "4":
            while True:
                for i in listOfStudents:
                    print(f"{i.name}\n{i.ID}\n")
                studentToView = input("Enter Student ID of Student to View: ")

                for student in listOfStudents:
                    if student.ID.getStudentID() == studentToView:
                        print(student.studentInfo())
                        # Display Student Courses
                        if student.getCourseList():
                            print("\n--- Courses ---")
                            print(student.getCourseList())
                        else:
                            print("\nNo courses found for this student.")
                        break
                else:
                    print("Student not found!")

                end = input("\nWould you like to view another student? (Y/N)\n")
                if end == "Y":
                    continue
                else:
                    break


        # Quit Program
        elif userInput == "5":
            print("You have selected to close the program!")
            break

    print("Thank you for using this program.")

if __name__ == "__main__":
    listOfStudents = []
    menu(listOfStudents)