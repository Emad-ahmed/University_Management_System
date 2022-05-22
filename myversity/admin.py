from distutils.log import Log
from django.contrib import admin
from myversity.models import Registration, Payment_Done, LoginSite, Student_All_Info, News, Events, Teacher

# Register your models here.


@admin.register(Registration)
class RegistrationDisplay(admin.ModelAdmin):
    list_display = ["id", "name", 'referece_number', "departMent"]


@admin.register(Payment_Done)
class RegistrationDisplay(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(LoginSite)
class LoginSiteDisplay(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Student_All_Info)
class Student_All_InfoDisplay(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(News)
class NewsDisplay(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Events)
class EventsDisplay(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Teacher)
class TeacherDisplay(admin.ModelAdmin):
    list_display = ["id"]
