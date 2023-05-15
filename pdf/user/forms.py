from django import forms
from .models import MyModel, Pdf

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ('pdf',)
        widgets = {
            'pdf': forms.FileInput(attrs={'accept': 'application/pdf'}),
        }