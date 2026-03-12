students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added")

def view_students():
    for s in students:
        print(s)

while True:
    print("1.Add 2.View 3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break