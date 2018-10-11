from django import forms
from django.utils.safestring import mark_safe

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]
class loginForm(forms.Form):
    uname = forms.CharField(label="Username ", max_length=100, required= False)
    pwd = forms.CharField(label=mark_safe("<br><br>Password "), max_length=100, widget=forms.PasswordInput, required= False) ##Password field

class DocHomeForm(forms.Form):
    pendingApp = forms.CharField(label="Pending Appointments ",widget=forms.Select(choices=FRUIT_CHOICES))
    reqApp = forms.CharField(label="Appointment Requests ",widget=forms.Select(choices='Select'))
