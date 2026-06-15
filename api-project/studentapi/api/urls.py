from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.get_students),
    path('students/<int:id>/', views.get_student),
]