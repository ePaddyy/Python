def get_score(assessment):

    while True:
        try:
            score = float(input(f"Enter {assessment} Score: "))

            if score < 0 or score > 100:
                print("Score must be between 0 and 100.")
                continue

            return score

        except ValueError:
            print("Please enter a valid number.")


def student_grader():

    weights = {
        "midterm": 20,
        "assignments": 20,
        "final_exam": 40,
        "project": 20
    }

    # Dictionary to store all students
    students = {}

    while True:

        print("\n" + "#" * 35)
        print("       WELCOME TO STUDENT GRADER")
        print("#" * 35)

        print("1. Add Student")
        print("2. Enter Scores")
        print("3. Calculate Grade")
        print("4. View Student")
        print("5. View All Students")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid input. Please enter a number from 1 to 6.")
            continue

        choice = int(choice)

        # ---------------------------------------
        # 1. Add Student
        # ---------------------------------------

        if choice == 1:

            name = input("Enter Student Name: ")

            if name in students:
                print("Student already exists.")

            else:
                students[name] = {
                    "midterm": 0,
                    "assignments": 0,
                    "final_exam": 0,
                    "project": 0,
                    "total": 0,
                    "grade": "Not calculated"
                }

                print(f"{name} has been added successfully.")

        # ---------------------------------------
        # 2. Enter Scores
        # ---------------------------------------

        elif choice == 2:

            name = input("Enter student name: ")

            if name not in students:
                print("Student not found. Please add the student first.")

            else:

                print(f"\nEntering scores for {name}")

                midterm = get_score("Midterm")
                assignments = get_score("Assignments")
                final_exam = get_score("Final Exam")
                project = get_score("Project")

                # Store scores in dictionary
                students[name]["midterm"] = midterm
                students[name]["assignments"] = assignments
                students[name]["final_exam"] = final_exam
                students[name]["project"] = project

                print("Scores saved successfully.")

        # ---------------------------------------
        # 3. Calculate Grade
        # ---------------------------------------

        elif choice == 3:

            name = input("Enter student name: ")

            if name not in students:
                print("Student not found.")

            else:

                student = students[name]

                total = (
                    student["midterm"] * weights["midterm"] / 100
                    + student["assignments"] * weights["assignments"] / 100
                    + student["final_exam"] * weights["final_exam"] / 100
                    + student["project"] * weights["project"] / 100
                )

                # Determine grade
                if total >= 80:
                    grade = "A"
                elif total >= 70:
                    grade = "B"
                elif total >= 60:
                    grade = "C"
                elif total >= 50:
                    grade = "D"
                else:
                    grade = "F"

                # Save results
                student["total"] = total
                student["grade"] = grade

                print("\nGrade calculated successfully!")
                print(f"Student: {name}")
                print(f"Total Score: {total:.2f}")
                print(f"Grade: {grade}")

        # ---------------------------------------
        # 4. View Student
        # ---------------------------------------

        elif choice == 4:

            name = input("Enter student name: ")

            if name not in students:
                print("Student not found.")

            else:

                student = students[name]

                print("\n" + "-" * 30)
                print(f"Student: {name}")
                print("-" * 30)

                print(f"Midterm:     {student['midterm']}")
                print(f"Assignments: {student['assignments']}")
                print(f"Final Exam:  {student['final_exam']}")
                print(f"Project:     {student['project']}")
                print(f"Total:       {student['total']:.2f}")
                print(f"Grade:       {student['grade']}")

        # ---------------------------------------
        # 5. View All Students
        # ---------------------------------------

        elif choice == 5:

            if not students:
                print("No students have been added yet.")

            else:

                print("\n" + "=" * 40)
                print("           ALL STUDENTS")
                print("=" * 40)

                for name, student in students.items():

                    print(
                        f"{name}: "
                        f"Total = {student['total']:.2f}, "
                        f"Grade = {student['grade']}"
                    )

        # ---------------------------------------
        # 6. Exit
        # ---------------------------------------

        elif choice == 6:

            print("Thank you for using Student Grader!")
            break


# Run the program
student_grader()