from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['student_id','name','email','study_field','gpa']

        labels = {
            'student_id': 'Student Roll',
            'name': 'Student Name',
            'email': 'Student Email',
            'study_field': 'Study Field',
            'gpa': 'Student GPA'
        }

        widgets = {
            'student_id': forms.NumberInput(attrs={'class':'form-control mb-3'}),
            'name': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'email': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'study_field': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'gpa': forms.NumberInput(attrs={'class':'form-control mb-3'})
        }