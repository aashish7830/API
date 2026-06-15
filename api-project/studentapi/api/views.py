from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

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

# GET All Students
def get_students(request):
    return JsonResponse(students, safe=False)


# GET Student By ID
def get_student(request, id):

    for student in students:
        if student["id"] == id:
            return JsonResponse(student)

    return JsonResponse(
        {"message": "Student not found"},
        status=404
    )