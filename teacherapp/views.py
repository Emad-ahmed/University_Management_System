from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from teacherapp.models import Course
from teacherapp.forms import CourseForm, CourseteacherForm, RseultForm
from django.contrib import messages
# Create your views here.


class HomeTeacher(View):
    def get(self, request):
        return render(request, 'base_teacher.html')


class CourseView(View):
    def get(self, request):
        course_main = Course.objects.all()

        return render(request, 'course.html', {'course': course_main})


class AssignCourseView(View):
    def get(self, request):
        form = CourseForm()
        return render(request, 'assign_course.html', {'form': form})

    def post(self, request):
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations!! Assigned Successfully')
            return redirect('course')
        else:
            messages.warning(request, 'Not Assign')
            return render(request, 'assign_course.html.html', {'form': form})


class AssignTeacherView(View):
    def get(self, request):
        form = CourseteacherForm()
        return render(request, 'assign.html', {'form': form})

    def post(self, request):
        form = CourseteacherForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations!! Assigned Successfully')
            return redirect('course')
        else:
            messages.warning(request, 'Not Assign')
            return render(request, 'assign.html.html', {'form': form})


class RseultView(View):
    def get(self, request):
        form = RseultForm()
        return render(request, 'assign.html', {'form': form})

    def post(self, request):
        form = RseultForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations!! Assigned Successfully')
            return redirect('result')
        else:
            messages.warning(request, 'Not Assign')
            return render(request, 'assign.html.html', {'form': form})
