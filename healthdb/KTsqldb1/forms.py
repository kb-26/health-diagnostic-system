from django import forms
from django.utils.safestring import mark_safe

class loginForm(forms.Form):
    uname = forms.CharField(label="Username ", max_length=100, required= False)
    pwd = forms.CharField(label=mark_safe("<br><br>Password "), max_length=100, widget=forms.PasswordInput, required= False) ##Password field