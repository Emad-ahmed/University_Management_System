import email
from django.shortcuts import render, redirect, HttpResponseRedirect

from django.contrib.auth.hashers import check_password
from myversity.models import Student_All_Info, LoginSite
from myversity.forms import StudentAllForm
from django.views import View
from django.contrib import messages


class StudentInfo(View):
    def get(self, request):
        fm = StudentAllForm()
        return render(request, 'student_info.html', {'form': fm})

    def post(self, request):
        student = request.session.get("email")
        myuser = LoginSite.objects.get(email=student)
        fm = StudentAllForm(request.POST, request.FILES)
        if fm.is_valid():
            obj = fm.save(commit=False)
            obj.user = myuser
            obj.save()
            request.session['student'] = myuser.id
            return redirect('home')
        return render(request, 'student_info.html', {'form': fm})
