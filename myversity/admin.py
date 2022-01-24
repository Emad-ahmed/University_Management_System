from django.contrib import admin
from myversity.models.registration import Registration

# Register your models here.


@admin.register(Registration)
class RegistrationDisplay(admin.ModelAdmin):
    list_display = ["id", "name", 'referece_number', "departMent"]
