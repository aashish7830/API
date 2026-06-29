from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import StudentForm
from .models import Student

def register(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        course = request.POST.get('course')

        Student.objects.create(
            name=name,
            email=email,
            course=course
        )

        return render(
            request,
            "success.html"
        )

    form = StudentForm()

    return render(
        request,
        "register.html",
        {'form': form}
    )