def get_score(assessment):
    while True:
        try:
            score = float(input(f"Enter {assessment} Score: "))

            if score <0 or score > 100:
                print("Score cannot be greater than 100. Enter correct score")
                continue

            return score
            
        except ValueError:
            print("Enter a valid number")

def get_name(students_dict):
    # Step 1: Prevent the infinite trap
    if not students_dict: 
        print("No students are in the system. Please add one first.")
        return None

    # Step 2: Start the loop
    while True:
        name = input("Enter student name (or type 'cancel' to go back): ").strip()

        # Step 3: The cancel hatch
        if name.lower() == 'cancel':
            return None

        # Step 4: The dictionary check
        if name in students_dict:
            return name
        else:
            print("Student not found. Please check the spelling and try again.")

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
        
            print("#" * 10)
            print("Welcome to Student Grader")
            print("#" * 10)

            print("Choose an Assessment")
            print("1. Add Student")
            print("2. Enter Scores")
            print("3. Calculate Grade")
            print("4. View Student")
            print("5. View All Students")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice not in ["1", "2", "3", "4", "5", "6"]:
                print("Invalid Input")
                print("Try again. Enter a number from 1 to 6")

            choice = int(choice)

            #-------------------------------------------------------
            # 1. Add Student
            #-------------------------------------------------------

            if choice == 1:

                name = str(input("Enter Student Name: "))

                if name in students:
                    print("Student already exits")

                else:
                    students[name] = {
                        "midterm": 0,
                        "assignments": 0,
                        "final exam": 0,
                        "project": 0,
                        "total": 0,
                        "grade": 0,
                    }

                    print(f"{name} has been added successfully")

            
            #-------------------------------------------------------
            # 2. Enter Scores
            #--------------------------------------------------------

            elif choice == 2:
                name = get_name(students)

                if name not in students:
                    print("\nStudent not found. Please add the student first.")
                                            
                else:

                    print(f"\nEntering scores for {name}")

                    midterm = get_score("midterm")
                    assignments = get_score("assignments")
                    final_exam = get_score("final_exam")
                    project = get_score("project")


                    # Store scores in dictionary
                    students[name]["midterm"] = midterm
                    students[name]["assignments"] = assignments
                    students[name]["final_exam"] = final_exam
                    students[name]["project"] = project
                    
                    print("score saved successfully")
                    
                                                                            
                    
            elif choice == 3:
                name = get_name(students)

                if name is None:
                    continue

                if name not in students:
                    print("Student not found.")

                else:
                    student = students[name]

                    total = (
                        student["midterm"] * (weights["midterm"] / 100)
                        + student["assignments"] * (weights["assignments"] / 100)
                        + student["final_exam"] * (weights["final_exam"] / 100)
                        + student["project"] * (weights["project"] / 100)
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

            elif choice == 4:
                name = get_name(students)

                if name is None:
                    continue

                if name not in students:
                    print("\nStudent not found. Please add the student first.")

                else:
                    print("\n" + "-" * 30)
                    print(f"Student: {name}")
                    print("-" * 30)

                    print(f"Midterm:        {students[name]['midterm']}")
                    print(f"assignments:    {students[name]['assignments']}")
                    print(f"final exam:     {students[name]['final_exam']}")
                    print(f"project:        {students[name]['project']}")
                    print(f"total:          {students[name]['total']:.2f}")
                    print(f"grade:          {students[name]['grade']}")


            # ---------------------------------------
            # 5. View All Students
            # ---------------------------------------
            
            elif choice == 5:
                if not students:
                    print("No students have been added yet.")
                else:
                    print("\n" + "=" * 40)
                    print("             ALL STUDENTS")
                    print("=" * 40)


                for name, student in students.items():

                    print(
                        f"{name}: "
                        f"Total = {student['total']:.2f}, "
                        f"Grade = {student['grade']}"
                    )

            # -----------------------------
            # 6. Exit
            # -----------------------------
            elif choice == "6":

                print("Thank you for using Student Grader!")

            else:
                print("Invalid choice. Please select 1-6.")
                break
            # -----------------------------
            # Invalid choice    
            # -----------------------------
            # else:
            #     print("Invalid choice. Please select 1-6.")      
                

# Run the program
student_grader()
