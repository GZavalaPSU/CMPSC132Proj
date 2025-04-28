from Advisor import Advisor

def AdvisorMenu(studentList):
    advisorList = [
        Advisor("Abby", "Brown", "C", "Professor", "Computer Science")  # Example advisor
    ]
    # List to store multiple advisors
    for student in studentList:
        if student.ID.getStudentID() in ["1234567890", "7203650189", "2470836766"]:  # Matching Student IDs
            advisorList[0].addAdvisee(student)

    while True:
        choice = input("\nAcademic Advisor Modification\n"
                       "Select an option:\n"
                       "1. Add Advisor\n"
                       "2. Display Advisors Info\n"
                       "3. Edit Advisor Info\n"
                       "4. Exit\n")

        if choice == "1":
            first = input("First Name: ")
            middle = input("Middle Name (or press Enter to skip): ")
            last = input("Last Name: ")
            title = input("Title (Professor, Instructor, Adjunct, etc.): ")
            department = input("Department: ")
            advisor = Advisor(first, last, middle, title, department)
            advisorList.append(advisor)  # Add the new advisor to the list
            print(f"Advisor {first} {last} added successfully.")

        elif choice == "2":
            if advisorList:
                print("\n--- Advisor Information ---")
                for i, adv in enumerate(advisorList):
                    print(f"{i + 1}. {adv}")  # Display all advisors with an index
            else:
                print("No advisors found. Please add one first.")

        elif choice == "3":
            if not advisorList:
                print("No advisors found. Please add one first.")
                continue

            # Display list of advisors to choose from
            print("\n--- Available Advisors ---")
            for i, adv in enumerate(advisorList):
                print(f"{i + 1}. {adv.getFirstName()} {adv.getLastName()} (Department: {adv.getDepartment()})")

            idx = int(input("Select an advisor to edit (number): ")) - 1
            if 0 <= idx < len(advisorList):
                selectedAdvisor = advisorList[idx]

                while True:
                    print("\n--- Edit Advisor ---")
                    print("1. Add Advisee")
                    print("2. Remove Advisee")
                    print("3. Back to Main Menu")
                    subChoice = input("Select an option: ")

                    if subChoice == "1":
                        # Select from listOfStudents
                        print("\nAvailable Students:")
                        for i, s in enumerate(studentList):
                            print(f"{i + 1}. {s.getName()} (ID: {s.getID()})")

                        studentIdx = int(input("Select student to add (number): ")) - 1
                        if 0 <= studentIdx < len(studentList):
                            selectedAdvisor.addAdvisee(studentList[studentIdx])
                            print("Student added to advisee list.")
                        else:
                            print("Invalid selection.")

                    elif subChoice == "2":
                        sid = input("Enter Student ID to remove: ")
                        if selectedAdvisor.removeAdvisee(sid):
                            print("Student removed.")
                        else:
                            print("Student not found.")

                    elif subChoice == "3":
                        break

                    else:
                        print("Invalid input.")
            else:
                print("Invalid advisor selection.")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid input.")