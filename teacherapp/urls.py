from django.urls import path
from teacherapp.views import HomeTeacher

urlpatterns = [
    path("", HomeTeacher.as_view(), name="home_teacher"),
]
