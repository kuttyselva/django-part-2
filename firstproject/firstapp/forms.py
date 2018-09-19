from django import forms
from firstapp.models import Exe

class NewUser(forms.ModelForm):
    class Meta():
        model= Exe
        fields='__all__'
