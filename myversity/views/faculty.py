import django
from django.shortcuts import render

from django.views import View
from myversity.models import Teacher


class BBAVIEW(View):
    def get(self, request):
        student = request.session.get("mystu")
        bba = Teacher.objects.filter(department='BBA')
        return render(request, 'faculty/bba.html', {'bba': bba, 'student': student})


class AllteachInfo(View):
    def get(self, request, id):
        student = request.session.get("mystu")
        tecahinfo = Teacher.objects.get(id=id)
        print(tecahinfo.eventsimg.url)
        print(tecahinfo.biography)
        print(tecahinfo.area_of_study)
        return render(request, 'faculty/allinfoteacher.html', {'tecahinfo': tecahinfo, 'student': student})


class CSEVIEW(View):
    def get(self, request):
        student = request.session.get("mystu")
        cse = Teacher.objects.filter(department='CSE')
        return render(request, 'faculty/cse.html', {'cse': cse, 'student': student})


class EEEVIEW(View):
    def get(self, request):
        student = request.session.get("mystu")
        eee = Teacher.objects.filter(department='EEE')
        return render(request, 'faculty/eee.html', {'eee': eee, 'student': student})
