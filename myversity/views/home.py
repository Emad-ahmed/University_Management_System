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
            alldata = {

                'allnews': mynews,
                'myevents': myevents,
            }
            return render(request, 'home.html', alldata)


class NewsView(View):
    def get(self, request, id):
        student = request.session.get("mystu")
        fullnews = News.objects.get(id=id)
        return render(request, 'fullnews.html', {'student': student, 'fullnews': fullnews})


class EventsView(View):
    def get(self, request, id):
        student = request.session.get("mystu")
        fullevents = Events.objects.get(id=id)
        print(fullevents.title)
        return render(request, 'eventsfull.html', {'student': student, 'fullevents': fullevents})
