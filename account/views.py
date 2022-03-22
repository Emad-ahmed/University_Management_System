import django
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from myversity.models.payment import Payment_Done

# Create your views here.


class HomeAccount(View):
    def get(self, request):
        return render(request, 'index.html')


class Addmission_Approve_View(View):
    def get(self, request):
        payment_done = Payment_Done.objects.all()
        return render(request, 'addmission_approve.html', {'payment_done': payment_done})
