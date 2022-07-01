from django.urls import path
from teacherapp.views import HomeTeacher, CourseView, AssignCourseView,  RseultView, AllRseultView, Deleteview, EditResultview, DeleteCourse, EditCourseview

urlpatterns = [
    path("", HomeTeacher.as_view(), name="home_teacher"),
    path("course", CourseView.as_view(), name="course"),
    path("assign", AssignCourseView.as_view(), name="assign"),

    path("result", RseultView.as_view(), name="result"),
    path("allresult", AllRseultView.as_view(), name="allresult"),
    path("delteresult/<int:id>/", Deleteview.as_view(), name="delteresult"),
    path("editresult/<int:id>/", EditResultview.as_view(), name="editresult"),
    path("deltecourse/<int:id>/", DeleteCourse.as_view(), name="deltecourse"),
    path("editcourse/<int:id>/", EditCourseview.as_view(), name="editcourse"),
]
