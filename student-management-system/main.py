import json

print("===== Student Management System =====")

try:
    with open("student.json", "r")as file:
        students = json.load(file)

except FileNotFoundError:
    students= {}

except json.JSONDecodeError:
    print("The file exists, but its contents are not valid JSON.")

    students = {}

while True:
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit \n")

    user_choice = input("Enter your choice: ")

    if user_choice == "1":

        student_id = input("Enter student ID: ")
        if student_id in students:
            print("Student ID already exists.")
        else:
            student_name =  input("Enter student name: ")
            student_age = int(input("Enter student age: "))
            student_course = input("Enter student course: ")

            students[student_id] = {
                "name" : student_name,
                "age": student_age,
                "course": student_course
            }

            with open("student.json", "w")as file:
                json.dump(students, file, indent=4)

            print("Student added successfully.")

    elif user_choice == "2":

        if not students:
            print("No student record found.")

        else:
            for student_id, info in students.items():
                print("=== Student Record ===")
                print(f"Student ID: {student_id}")
                print(f'Student Name: {info["name"]}')
                print(f'Student Age: {info["age"]}')
                print(f'Student Course: {info["course"]}')

    elif user_choice == "3":
        student_id = input("Enter Student ID: ")

        if student_id in students:
            info = students[student_id]

            print("=== Student Record ===")
            print(f"Student ID: {student_id}")
            print(f'Student Name: {info["name"]}')
            print(f'Student Age: {info["age"]}')
            print(f'Student Course: {info["course"]}')

        else:
            print("Student not found.")

    elif user_choice == "4":

        student_id = input("Enter your student ID: ")

        if student_id in students:
            print("Choose to what you wanted to update.")
            print("1. Name")
            print("2. Age")
            print("3. Course")

            user_update = input("Enter your choice: ")

            if user_update == "1":
                new_name = input("Enter a new name: ")
                students[student_id]["name"] = new_name
                print(f"Updated name: {students[student_id]['name']}")
            elif user_update == "2":
                new_age = int(input("Enter a new age: "))
                students[student_id]["age"] = new_age
                print(f"Updated age: {students[student_id]['age']}")
            elif user_update == "3":
                new_course = input("Enter your new course: ")
                students[student_id]["course"] = new_course
                print(f"Updated course: {students[student_id]['course']}")

            else:
                print("Not in the choices.")

            if user_update in ["1", "2", "3"]:
                with open("student.json", "w") as file:
                    json.dump(students, file, indent=4)

                print("Student information updated successfully!")


            else:
                print("Student ID does not exist.")

    elif user_choice == "5":

        student_id = input("Enter your student ID: ")

        if student_id in students:
            student_del = input(
                'Are you sure you want to delete this student? (Enter "Yes" to confirm or "No" to cancel): '
            ).strip().lower()

            if student_del == "yes":
                students.pop(student_id)

                with open("student.json", "w") as file:
                    json.dump(students, file, indent=4)

                print("Deleted successfully.")

            elif student_del == "no":
                print("Canceled.")

            else:
                print("Invalid confirmation. Please enter Yes or No.")

        else:
            print("Student ID does not exist.")


    elif user_choice == "6":
        print("Exiting Student Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
