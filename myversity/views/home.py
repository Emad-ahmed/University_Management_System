from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from myversity.models import Student_All_Info, LoginSite, Registration, News, Events


class HomeView(View):
    def get(self, request):
        student = request.session.get("mystu")
        myinfo = Registration.objects.filter(email=student)
        mynews = News.objects.filter()[:6]
        myevents = Events.objects.filter()[:6]
        alldata = {
            'student': student,
            'allnews': mynews,
            'myevents': myevents,
        }
        if myinfo:
            return render(request, 'home.html', alldata)
        else:
            return redirect("loginview")
