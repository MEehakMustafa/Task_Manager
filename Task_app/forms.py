from django import forms
from .models import task

class TaskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['task_name', 'is_done']  # Specify the fields you want in the form
