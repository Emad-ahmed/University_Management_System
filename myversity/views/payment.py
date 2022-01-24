from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View


class PaymentView(View):
    def get(self, request):
        return render(request, 'payment.html')

    def post(self, request):
        return render(request, 'payment.html')
