from django import forms

from .models import *

class additemform(forms.ModelForm):
    class Meta:
        model=items
        fields="__all__"