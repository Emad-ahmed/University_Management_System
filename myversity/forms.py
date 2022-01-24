from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from django.forms import fields, widgets
from django.core import validators
from django.utils.translation import ugettext, ugettext_lazy as _
from myversity.models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('name',  'phone', 'email',
                  'departMent', 'ssc_gpa', 'hsc_gpa')
        labels = {'email': "Email", 'departMent': "Department",
                  }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'departMent': forms.TextInput(attrs={'class': 'form-control'}),
            'ssc_gpa': forms.NumberInput(attrs={'class': 'form-control'}),
            'hsc_gpa': forms.NumberInput(attrs={'class': 'form-control'}),
            'msg_txt': forms.Textarea(attrs={'class': 'form-control'}),
        }
