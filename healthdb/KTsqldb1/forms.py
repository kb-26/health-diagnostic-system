from django import forms
from django.utils.safestring import mark_safe

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

#basic login form
class loginForm(forms.Form):
    uname = forms.CharField(label="Username ", max_length=30)
    pwd = forms.CharField(label=mark_safe("Password "), max_length=30, widget=forms.PasswordInput) ##Password field

#Doctor home page
class DocHomeForm(forms.Form):
    pendingApp = forms.CharField(label="Pending Appointments ",widget=forms.Select(choices=FRUIT_CHOICES))
    reqApp = forms.CharField(label="Appointment Requests ",widget=forms.Select(choices='Select'))
