import email
import imp
from django.conf import Settings
from django.db.models.query_utils import subclasses
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from myversity.models.registration import Registration
from django.core.mail import send_mail
from myversity.forms import RegistrationForm
from django.contrib import messages
from django.conf import settings
import http.client
from rest_framework.decorators import api_view
import requests


class RegisterView(View):
    def get(self, request):
        fm = RegistrationForm()
        return render(request, 'register.html', {'form': fm})

    def post(self, request):
        fm = RegistrationForm(request.POST)

        if fm.is_valid():
            myemail = fm.cleaned_data["email"]
            fm.save()
            messages.success(request, 'Profile details updated.')

            try:
                myuser = Registration.objects.get(email=myemail)
            except:
                myuser = None

            content = f"Hello {myuser.name}\nYour Registration Has Been Successfull.\nPay 500 For The Form Fee and Use This {myuser.referece_number} Code As A Refernce Number Thanks For Registration.Use This Link For Pay http://127.0.0.1:8000/payment/{myuser.id}\n\nLeading University, Sylhet"
            send_mail("Successfully Registration",
                      content,
                      settings.EMAIL_HOST_USER,
                      [myemail]
                      )
            return render(request, 'register.html', {'form': fm})

        else:
            messages.error(request, "Not Valid")
            return render(request, 'register.html', {'form': fm})
