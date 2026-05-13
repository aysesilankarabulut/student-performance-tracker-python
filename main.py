import json
import os


FILE_NAME = "students.json"
students = []


def load_students():
    global students

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            students = json.load(file)
    else:
        students = []


def save_students():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

def get_valid_grade():
    while True:
        try:
            grade = float(input("Enter student grade: "))

            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    grade = get_valid_grade()

    student = {
        "name": name,
        "grade": grade
    }

    students.append(student)
    save_students()

    print("Student added and saved successfully.")

def show_students():
    if not students:
        print("No students found.")
        return

    print("\nStudent List:")
    for student in students:
        print(f"Name: {student['name']} - Grade: {student['grade']}")


def calculate_average():
    if not students:
        print("No grades available.")
        return

    total = sum(student["grade"] for student in students)
    average = total / len(students)

    print(f"Class average: {average:.2f}")


def delete_student():
    if not students:
        print("No students found.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    for student in students:
        if student['name'].lower() == name.lower():
            students.remove(student)
            save_students()
            print("Student deleted successfully.")
            return

    print("Student not found.")


def update_student_grade():
    if not students:
        print("No students found.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    for student in students:
        if student['name'].lower() == name.lower():
            new_grade = get_valid_grade()
            student['grade'] = new_grade
            save_students()
            print("Student grade updated successfully.")
            return

    print("Student not found.")


def show_highest_lowest_grade():
    if not students:
        print("No students found.")
        return

    highest_student = max(students, key=lambda student: student['grade'])
    lowest_student = min(students, key=lambda student: student['grade'])

    print(f"\nHighest Grade: {highest_student['name']} - {highest_student['grade']}")
    print(f"Lowest Grade: {lowest_student['name']} - {lowest_student['grade']}")


def search_student():
    if not students:
        print("No students found.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    for student in students:
        if student['name'].lower() == name.lower():
            print(f"Student found: {student['name']} - Grade: {student['grade']}")
            return

    print("Student not found.")


def main():
    load_students()

    while True:
        print("\nStudent Performance Tracker")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Calculate Average")
        print("4. Delete Student")
        print("5. Update Student Grade")
        print("6. Show Highest and Lowest Grade")
        print("7. Search Student")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student_grade()
        elif choice == "6":
            show_highest_lowest_grade()
        elif choice == "7":
            search_student()
        elif choice == "8":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()