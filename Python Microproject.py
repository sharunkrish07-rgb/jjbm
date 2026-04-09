students = {}

valid_grades = ["A","B","C","D","A+","B+","C+","D+","A-","B-","C-","D-","F"]

def get_number_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return value
        else:
            print("Only numbers are allowed.")

def get_name_input(prompt):
    while True:
        value = input(prompt)
        if all(part.isalpha() for part in value.split()):
            return value
        else:
            print("Name should contain letters only (spaces allowed).")

def get_age_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and 16 <= int(value) <= 100:
            return value
        else:
            print("Enter a valid age.")

def get_grade_input(prompt):
    while True:
        value = input(prompt).upper()
        if value in valid_grades:
            return value
        else:
            print("Invalid grade.")


def add_student():
    sid = get_number_input("Enter Student ID: ")

    if sid in students:
        print("Student ID already exists. Try another ID.\n")
        return

    name = get_name_input("Enter Name: ")
    age = get_age_input("Enter Age: ")
    grade = get_grade_input("Enter Grade: ")

    students[sid] = {"name": name, "age": age, "grade": grade}
    print("Student added successfully\n")


def search_student():
    sid = get_number_input("Enter Student ID to search: ")

    if sid in students:
        print("\nStudent Found")
        print("Name:", students[sid]["name"])
        print("Age:", students[sid]["age"])
        print("Grade:", students[sid]["grade"])
    else:
        print("Student not found\n")


def update_student():
    sid = get_number_input("Enter Student ID to update: ")

    if sid in students:
        name = get_name_input("Enter new name: ")
        age = get_age_input("Enter new age: ")
        grade = get_grade_input("Enter new grade: ")

        students[sid] = {"name": name, "age": age, "grade": grade}
        print("Record updated successfully\n")
    else:
        print("Student not found\n")


def delete_student():
    sid = get_number_input("Enter Student ID to delete: ")

    if sid in students:
        del students[sid]
        print("Student record deleted successfully\n")
    else:
        print("Student not found\n")


def display_students():
    if not students:
        print("No records found\n")
        return

    print("\nAll Student Records")
    for sid, details in students.items():
        print("ID:", sid)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Grade:", details["grade"])
        print("--------------------")


while True:
    print("\nSTUDENT RECORD SYSTEM")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Display All Students")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        update_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
