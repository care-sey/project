import json

print("===== Student Management System =====")

try:

    with open("student.json", "r") as file:
        students = json.load(file)

except FileNotFoundError:
    students = {}

except json.JSONDecodeError:
   print("The file exists, but its contents are not valid JSON.")

   students= {}

#loops and condition together with choices
while True:
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit \n")

    user_choice = input("Enter your choice: \n")

    if user_choice == "1":

        student_id = input(" Enter Student ID: ")
        if student_id in students:
            print("Student ID already exists!")
        else:
            student_name = input("Enter student name: ")
            student_age = int(input("Enter student age: "))
            student_course = input("Enter student course: ")

            students[student_id] = {
                "name" : student_name,
                "age" : student_age,
                "course" : student_course
            }


            with open("student.json", "w") as file:
                json.dump(students, file, indent=4)

            print("Student added successfully!")

    elif user_choice == "2":

        if not students:
            print("No student records found.")

        else:
            for student_id, info in students.items():

                print("=== Student Record ===")
                print(f"Student ID: {student_id}")
                print(f'Student Name: {info["name"]}')
                print(f'Student Age: {info["age"]}')
                print(f'Student Course: {info["course"]}')


        print("View All Students selected!")

    elif user_choice == "3":
        print("Search Student selected")
    elif user_choice == "4":
        print("Update Student selected!")
    elif user_choice == "5":
        print("Delete Student selected!")
    elif user_choice == "6":
        print("Exiting Student Management System. Goodbye! ")
        break
    else:
        print("Invalid choice. Please try again. ")



