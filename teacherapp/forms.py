from django import forms
from django.forms import fields, widgets
from django.core import validators

from teacherapp.models import Course, CourseAssign, Result


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_code',  'course_name', 'credit',
                  'description', 'deparetment', 'semister')
        labels = {'departMent': "Select the Department",

                  }
        widgets = {
            'course_code': forms.TextInput(attrs={'class': 'form-control'}),
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'credit': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'deparetment': forms.Select(attrs={'class': 'form-control'}),
            'semister': forms.Select(attrs={'class': 'form-control'}),

        }


class CourseteacherForm(forms.ModelForm):
    class Meta:
        model = CourseAssign
        fields = ('department',  'teacher', 'course')

        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
        }


class RseultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('student',  'id_no', 'department', 'course', 'select_grade')

        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'id_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'select_grade': forms.Select(attrs={'class': 'form-control'}),
        }
