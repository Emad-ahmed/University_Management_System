import django
from django.shortcuts import render

from django.views import View


class BBAVIEW(View):
    def get(self, request):
        return render(request, 'faculty/bba.html')
