from flask import Flask, request, jsonify
import sqlite3
from database import create_table

app = Flask(__name__)

DB_NAME = "students.db"

create_table()

def connect():
    return sqlite3.connect(DB_NAME)


@app.route("/students", methods=["POST"])
def add_student():

    data = request.json

    student_id = data["id"]
    name = data["name"]
    age = data["age"]
    course = data["course"]

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?)",
        (student_id, name, age, course)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Student added"})


@app.route("/students", methods=["GET"])
def get_students():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    result = []

    for s in students:
        result.append({
            "id": s[0],
            "name": s[1],
            "age": s[2],
            "course": s[3]
        })

    conn.close()

    return jsonify(result)


@app.route("/students/<student_id>", methods=["GET"])
def get_student(student_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    conn.close()

    if student:
        return jsonify({
            "id": student[0],
            "name": student[1],
            "age": student[2],
            "course": student[3]
        })

    return jsonify({"message": "Student not found"})


@app.route("/students/<student_id>", methods=["DELETE"])
def delete_student(student_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"message": "Student not found"})

    conn.close()

    return jsonify({"message": "Student deleted"})


if __name__ == "__main__":
    app.run(debug=True)