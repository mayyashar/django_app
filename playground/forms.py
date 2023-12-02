from django import forms
from .models import FormData

class createNewList(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['name', 'age', 'healthy', 'fever', 'Blood_Pressure', 'specify']