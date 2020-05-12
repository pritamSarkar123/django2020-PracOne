from django import forms
from .models import WebUser


class NewUserForm(forms.ModelForm):
    class Meta:
        model = WebUser
        fields = '__all__'
