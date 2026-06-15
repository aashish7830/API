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
    },
    {
        "id": 3,
        "name": "Mohit",
        "course": "MCA"
    }
]

def get_students(request):
    return JsonResponse(students, safe=False)