from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
