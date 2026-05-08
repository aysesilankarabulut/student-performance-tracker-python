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


def main():
    load_students()

    while True:
        print("\nStudent Performance Tracker")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Calculate Average")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()