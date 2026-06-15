from django.shortcuts import render

# Create your views here.
from django.db import connection
from django.shortcuts import render

from django.db import connection
from django.http import HttpResponse

def student_list(request):

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

    return HttpResponse(str(rows))