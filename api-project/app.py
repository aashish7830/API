from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Aashish",
        "course": "B.Tech CSE DS"
    },
    {
        "id": 2,
        "name": "Rahul",
        "course": "BCA"
    }
]

# GET all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# GET student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)