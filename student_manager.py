import json

students = []

FILE_NAME = "students.json"


def load_students():
    global students
    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    except:
        students = []


def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    print("\nAdd New Student")

    student_id = input("Enter student ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    print("Student added successfully!")


def view_students():

    if not students:
        print("No students found.")
        return

    print("\nStudent List")
    print("---------------------------")

    for student in students:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print("---------------------------")


def search_student():

    search_id = input("Enter student ID to search: ")

    for student in students:
        if student["id"] == search_id:
            print("\nStudent Found")
            print(student)
            return

    print("Student not found.")


def delete_student():

    delete_id = input("Enter student ID to delete: ")

    for student in students:
        if student["id"] == delete_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")