import email
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from myversity.models import Student_All_Info, Registration
from myversity.forms import StudentAllForm
from django.views import View
from myversity.models.loginregister import LoginSite
from django.contrib import messages


class StudentInfo(View):
    def get(self, request):
        n = request.session.get("email")
        fm = StudentAllForm()
        return render(request, 'student_info.html', {'form': fm})

    def post(self, request):
        student = request.session.get("email")
        myuser = Registration.objects.get(email=student)
        fm = StudentAllForm(request.POST, request.FILES)
        if fm.is_valid():
            obj = fm.save(commit=False)
            obj.user = myuser
            obj.save()
            request.session['student'] = myuser.email
            messages.success(
                request, "Successfully Assign Student Info Now You Can Login")
            return redirect('home')
        return render(request, 'student_info.html', {'form': fm})
