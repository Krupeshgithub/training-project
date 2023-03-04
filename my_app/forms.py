from dataclasses import field
from django import forms
from .models import *

    
class SubjectForm(forms.ModelForm):
    class Meta:
        model = subject
        fields = "__all__"

class TeacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields  = ['teacher_name']

class StudentForms(forms.ModelForm):
    class Meta:
        model = student
        fields  = "__all__"