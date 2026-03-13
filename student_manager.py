from database import connect

def add_student():

    student_id = input("Enter student ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?)",
        (student_id, name, age, course)
    )

    conn.commit()
    conn.close()

    print("Student added successfully")


def view_students():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if not students:
        print("No students found")
        return

    for student in students:
        print("--------------------")
        print("ID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Course:", student[3])

    conn.close()


def search_student():

    student_id = input("Enter student ID: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("Student found")
        print(student)
    else:
        print("Student not found")

    conn.close()


def delete_student():

    student_id = input("Enter student ID to delete: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        print("Student not found")
    else:
        print("Student deleted")

    conn.close()