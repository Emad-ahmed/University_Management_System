from django.urls import path
from teacherapp.views import HomeTeacher, CourseView, AssignCourseView, AssignTeacherView, RseultView

urlpatterns = [
    path("", HomeTeacher.as_view(), name="home_teacher"),
    path("course", CourseView.as_view(), name="course"),
    path("assign", AssignCourseView.as_view(), name="assign"),
    path("assign_teacher", AssignTeacherView.as_view(), name="assign_teacher"),
    path("result", RseultView.as_view(), name="result"),
]
