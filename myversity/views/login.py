from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from myversity.models import LoginSite, Student_All_Info, Registration
from django.views import View
from django.contrib import messages


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        student = Registration.get_student_by_email(email)

        try:
            mystudent = Student_All_Info.objects.get(user=student)
        except:
            mystudent = None
        print(mystudent)
        if student:
            if student.email == email:
                if mystudent:
                    request.session['mystu'] = mystudent.user.email
                    return redirect("home")
                else:
                    request.session['email'] = email
                    return redirect('studentallinfo')
            else:
                messages.warning(request, "Email and Password Invalid!")
        elif((email == "teacher231@gmail.com" and password == "teacher45632") or (email == "faruq@gmail.com" and password == "1234567")):
            request.session['teacher'] = "teacher231@gmail.com"
            request.session['teacher'] = "faruq@gmail.com"
            return redirect("/teacher/")
        elif(email == "account34567@gmail.com" and password == "account234"):
            request.session['account'] = "account34567@gmail.com"
            return redirect("/account/")

        else:
            messages.warning(request, "Email and Password Invalid!")

        return render(request, 'login.html')


def logout(request):
    request.session.clear()
    return redirect('loginview')
