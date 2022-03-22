from django.contrib import admin
from myversity.models import Registration, Payment_Done

# Register your models here.


@admin.register(Registration)
class RegistrationDisplay(admin.ModelAdmin):
    list_display = ["id", "name", 'referece_number', "departMent"]


@admin.register(Payment_Done)
class RegistrationDisplay(admin.ModelAdmin):
    list_display = ["id"]
