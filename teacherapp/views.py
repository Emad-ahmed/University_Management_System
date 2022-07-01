from cmath import pi
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from teacherapp.models import Course
from myversity.models import Teacher
from teacherapp.forms import CourseForm, CourseteacherForm, RseultForm
from django.contrib import messages
from teacherapp.models import Result
# Create your views here.


class HomeTeacher(View):
    def get(self, request):
        allteacher = Teacher.objects.all()
        return render(request, 'teacher_view.html', {'allteacher': allteacher})


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
            return render(request, 'assign_course.html', {'form': form})


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
            return render(request, 'assign.html', {'form': form})


class AllRseultView(View):
    def get(self, request):
        allresult = Result.objects.all()
        return render(request, 'allresultview.html', {'allresult': allresult})


class Deleteview(View):
    def get(self, request, id):
        studentresult = Result.objects.get(id=id)
        studentresult.delete()
        messages.warning(request, "delete successfully")
        return redirect("allresult")


class EditResultview(View):
    def get(self, request, id):
        pi = Result.objects.get(id=id)
        form = RseultForm(instance=pi)
        return render(request, 'update_result.html', {'form': form})

    def post(self, request, id):
        pi = Result.objects.get(id=id)
        form = RseultForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations!! Updated Successfully')
            return redirect('allresult')
        else:
            messages.warning(request, 'Not Updated')
        return render(request, 'update_result.html', {'form': form})


class DeleteCourse(View):
    def get(self, request, id):
        studentcourse = Course.objects.get(id=id)
        studentcourse.delete()
        messages.success(request, "delete successfully")
        return redirect("course")


class EditCourseview(View):
    def get(self, request, id):
        pi = Course.objects.get(id=id)
        form = CourseForm(instance=pi)
        return render(request, 'editcourse.html', {'form': form})

    def post(self, request, id):
        pi = Course.objects.get(id=id)
        form = CourseForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations!! Updated Successfully')
            return redirect('course')
        else:
            messages.warning(request, 'Not Updated')
        return render(request, 'editcourse.html', {'form': form})
