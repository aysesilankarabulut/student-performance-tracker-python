students = []


def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))

    student = {
        "name": name,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully.")


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