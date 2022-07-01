import imp
import django
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from myversity.models.payment import Payment_Done
from myversity.models.loginregister import LoginSite
from myversity.forms import StudentAllForm
from django.conf import settings
from django.core.mail import send_mail
import random
import string
import string
import random
from myversity.models.studentallinfo import Student_All_Info
from django.contrib import messages

length = 5


# python3
randomstr = ''.join(random.choices(
    string.ascii_letters+string.digits, k=length))


class HomeAccount(View):
    def get(self, request):
        account = request.session.get("account")
        if account:
            myinfo = Student_All_Info.objects.all()
            print(myinfo)
            return render(request, 'addmission_accept.html', {'info': myinfo})
        else:
            return redirect("loginview/")


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

        return redirect("addmission_approve")


class UpdateAdmission(View):
    def get(self, request, id):
        studentinfo = Student_All_Info.objects.get(id=id)
        form = StudentAllForm(instance=studentinfo)
        return render(request, 'show_details_addmission.html', {'form': form, 'id': id})

    def post(self, request, id):
        studentinfo = Student_All_Info.objects.get(id=id)
        form = StudentAllForm(request.POST, request.FILES,
                              instance=studentinfo)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Saved")
            return redirect("/account")
        else:
            return HttpResponse("Not")

        return render(request, 'show_details_addmission.html', {'form': form})


def deleteadmission(request, id):
    studentinfo = Student_All_Info.objects.get(id=id)
    studentinfo.delete()

    return redirect("/account")
