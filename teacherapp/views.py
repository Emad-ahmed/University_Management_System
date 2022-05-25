from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


class HomeTeacher(View):
    def get(self, request):
        return render(request, 'base_teacher.html')
