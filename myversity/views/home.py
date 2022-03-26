from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from myversity.models import Student_All_Info, LoginSite


class HomeView(View):
    def get(self, request):
        student = request.session.get("student")
        if student:
            return render(request, 'home.html', {'student': student})
        else:
            return redirect("loginview")
