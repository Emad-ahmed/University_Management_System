from django.shortcuts import render, redirect, HttpResponseRedirect

from django.contrib.auth.hashers import check_password
from myversity.models import LoginSite, Student_All_Info
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
        student = LoginSite.get_student_by_email(email)
        try:
            mystudent = Student_All_Info.objects.get(user=student)
        except:
            mystudent = None
        if student:
            if student.password == password:
                if mystudent:
                    request.session['student'] = student.id
                    return redirect("home")

                request.session['email'] = email
                return redirect('studentallinfo')
            else:
                messages.warning(request, "Email and Password Invalid!")
        elif(email == "account34567@gmail.com" and password == "account234"):
            return render(request, 'index.html')

        else:
            messages.warning(request, "Email and Password Invalid!")

        return render(request, 'login.html')


def logout(request):
    request.session.clear()
    return redirect('loginview')
