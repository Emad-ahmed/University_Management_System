from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from django.forms import fields, widgets
from django.core import validators

from myversity.models import Registration, Student_All_Info


class DatePickerInput(forms.DateInput):
    input_type = 'date'
    id = "form-control"


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('name',  'phone', 'email',
                  'departMent', 'ssc_gpa', 'hsc_gpa')
        labels = {'email': "Email", 'departMent': "Department", "phone": "Mobile"
                  }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'departMent': forms.Select(attrs={'class': 'form-control'}),
            'ssc_gpa': forms.NumberInput(attrs={'class': 'form-control'}),
            'hsc_gpa': forms.NumberInput(attrs={'class': 'form-control'}),
            'msg_txt': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = Registration.objects.get(email=email)
        except Registration.DoesNotExist:
            return email

        raise forms.ValidationError('This email address is already in use.')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        try:
            match = Registration.objects.get(phone=phone)

        except Registration.DoesNotExist:
            return phone

        raise forms.ValidationError(
            'This Phone Number  is already in use.')


class StudentAllForm(forms.ModelForm):
    class Meta:
        model = Student_All_Info
        fields = ('departMent',  'father_name', 'mother_name',
                  'maritial_status', 'blood_Group', 'national_id', 'd_o_birth', 'gender', 'religion', 'nationality', 'guardians_name', 'guardians_con_no', 'permanent_address', 'present_address', 'registration_no_of_ssc', 'name_of_instituin_ssc', 'roll_ssc', 'group_ssc', 'Board_ssc', 'gpa_ssc', 'registration_no_of_hsc', 'name_of_instituin_hsc', 'roll_hsc', 'group_hsc', 'Board_hsc', 'gpa_hsc', 'student_Img')
        labels = {'departMent': "Select the Department",
                  'father_name': "Father Name(Full Name)",
                  'mother_name': "Mother Name(Full Name)",
                  'maritial_status': "Marital Status",
                  'blood_Group': "Blood Group",
                  'national_id': "National ID/Birth Certificate No.",
                  'd_o_birth': 'Applicant,s Date Of Birth',
                  'gender': 'Gender',
                  'religion': "Religion",

                  'guardians_name': "Guardian's Name",
                  'guardians_con_no': "Guardian's Contact No",
                  'permanent_address': "Permanent Address",
                  'present_address': "Present Address",
                  'registration_no_of_ssc': "Registration no.of.SSC",
                  'name_of_instituin_ssc': "Name of the institution (SSC)",
                  'roll_ssc': "Roll",
                  'group_ssc': "Group",
                  'year_ssc': "Year",
                  'Board_ssc': "Board",
                  'gpa_ssc': "GPA",
                  'registration_no_of_hsc': "Registration no.of.HSC",
                  'name_of_instituin_hsc': "Name of the institution (HSC)",
                  'roll_hsc': "Roll",
                  'group_hsc': "Group",
                  'year_hsc': "Year",
                  'Board_hsc': "Board",
                  'gpa_hsc': "GPA",
                  'student_Img': "Upload Applicant's Photo(Max 1 MB)",

                  }
        widgets = {
            'departMent': forms.Select(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'maritial_status': forms.Select(attrs={'class': 'form-control'}),
            'blood_Group': forms.TextInput(attrs={'class': 'form-control'}),
            'national_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'd_o_birth': DatePickerInput(),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'religion': forms.Select(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'guardians_name': forms.TextInput(attrs={'class': 'form-control'}),
            'guardians_con_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'permanent_address': forms.Textarea(attrs={'class': 'form-control'}),
            'present_address': forms.Textarea(attrs={'class': 'form-control'}),
            'registration_no_of_ssc': forms.NumberInput(attrs={'class': 'form-control'}),
            'name_of_instituin_ssc': forms.TextInput(attrs={'class': 'form-control'}),
            'roll_ssc': forms.NumberInput(attrs={'class': 'form-control'}),
            'group_ssc': forms.Select(attrs={'class': 'form-control'}),
            'year_ssc': forms.Select(attrs={'class': 'form-control'}),
            'Board_ssc': forms.Select(attrs={'class': 'form-control'}),
            'gpa_ssc': forms.NumberInput(attrs={'class': 'form-control'}),
            'registration_no_of_hsc': forms.NumberInput(attrs={'class': 'form-control'}),
            'name_of_instituin_hsc': forms.TextInput(attrs={'class': 'form-control'}),
            'roll_hsc': forms.NumberInput(attrs={'class': 'form-control'}),
            'group_hsc': forms.Select(attrs={'class': 'form-control'}),
            'year_ssc': forms.Select(attrs={'class': 'form-control'}),
            'Board_hsc': forms.Select(attrs={'class': 'form-control'}),
            'gpa_hsc': forms.NumberInput(attrs={'class': 'form-control'}),
            'student_Img': forms.FileInput(attrs={'class': 'form-control'}),
        }
