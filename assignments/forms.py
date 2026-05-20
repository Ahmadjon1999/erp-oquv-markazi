from django import forms
from .models import Submission, Grade



class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['file', 'text']


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['score', 'feedback']
