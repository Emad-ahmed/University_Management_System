import imp
import django
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from myversity.models.payment import Payment_Done
from myversity.models.loginregister import LoginSite
from django.conf import settings
# Create your views here.
from django.core.mail import send_mail
import random
import string
import string
import random

from myversity.models.studentallinfo import Student_All_Info

length = 5


# python3
randomstr = ''.join(random.choices(
    string.ascii_letters+string.digits, k=length))


class HomeAccount(View):
    def get(self, request):
        myinfo = Student_All_Info.objects.all()
        print(myinfo)
        return render(request, 'index.html', {'info': myinfo})


class Addmission_Approve_View(View):
    def get(self, request):
        payment_done = Payment_Done.objects.all()
        print(payment_done)
        return render(request, 'addmission_approve.html', {'payment_done': payment_done})


class Approve_RegisterView(View):
    def get(self, request, id):
        payment_done = Payment_Done.objects.all()
        myuser = Payment_Done.objects.get(id=id)
        email = myuser.user.email

        length = 7
        randomstr = ''.join(random.choices(
            string.ascii_letters+string.digits, k=length))
        password = randomstr

        loginuser = LoginSite(email=email, password=password)
        loginuser.save()

        content = f"Now You Can Login\nYour Email Is {email}\nPassword: {password}\nNow You can Login http://127.0.0.1:8000/loginview/"
        send_mail("Successfully Registration",
                  content,
                  settings.EMAIL_HOST_USER,
                  [email]
                  )
        myuser.delete()
        print(payment_done)
        return redirect("addmission_approve")
