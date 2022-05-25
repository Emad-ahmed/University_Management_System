from distutils.log import Log
from django.contrib import admin
from myversity.models.faculty import Teacher
from teacherapp.models import Deparetment, Course

# Register your models here.


@admin.register(Deparetment)
class DepartmentDisplay(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Course)
class CourseDisplay(admin.ModelAdmin):
    list_display = ["id"]
