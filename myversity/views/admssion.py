from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View


class AboutView(View):
    def get(self, request):
        student = request.session.get("mystu")
        return render(request, 'admssion/admission_policies.html', {'student': student})


class ScholarView(View):
    def get(self, request):
        student = request.session.get("mystu")
        return render(request, 'admssion/scholarship.html', {'student': student})


class TutionFeesView(View):
    def get(self, request):
        student = request.session.get("mystu")
        return render(request, 'admssion/tutioon_fees.html', {'student': student})


class GuideLineView(View):
    def get(self, request):
        student = request.session.get("mystu")
        return render(request, 'admssion/guideline.html', {'student': student})
