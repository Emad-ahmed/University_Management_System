from django.db.models.query_utils import subclasses
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from myversity.models.registration import Registration
from django.core.mail import send_mail
from myversity.forms import RegistrationForm
from django.contrib import messages


class RegisterView(View):
    def get(self, request):
        fm = RegistrationForm()
        return render(request, 'register.html', {'form': fm})

    def post(self, request):
        try:
            fm = RegistrationForm(request.POST)
            if fm.is_valid():
                myemail = fm.cleaned_data["email"]
                fm.save()
            myobject = Registration.objects.get(email=myemail)
            ref_no = myobject.referece_number
            my_name = myobject.name
            my_department = myobject.departMent
            myobjectemail = myobject.email
            message = f'Name: {my_name}\nDepartment : {my_department}\nYour Reference Number Is {ref_no}.\n To Get Payment Click This Link "http://127.0.0.1:8000/payment/"'

            subject = "Successfully Register"
            my_message = message
            from_email = 'emadahmednew123456789@gmail.com'
            to_email = [myobjectemail]
            send_mail(subject, my_message, from_email, to_email)
            messages.success(request, 'Profile details updated.')
            return render(request, 'register.html', {'form': fm})
        except:
            return render(request, 'register.html', {'form': fm})
