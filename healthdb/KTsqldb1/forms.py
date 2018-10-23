from django import forms
import datetime
from django.utils.safestring import mark_safe
from django.forms.widgets import SelectDateWidget
from django.core.validators import MaxValueValidator


from KTsqldb1.ServiceLogic.queries import getDocList
from .constants import res


FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

# Basic login form
class loginForm(forms.Form):
    uname = forms.CharField(label="Username ", max_length=30)
    pwd = forms.CharField(label=mark_safe("Password "), max_length=30, widget=forms.PasswordInput,
                          error_messages = {'authFail':'Username or Password Incorrect'}) ##Password field

    # def clean_pwd(self):  # Throw invalid password exception
    #     if res==False:
    #         raise ValidationError(self.fields['pwd'].error_messages['authFail'])


# Doctor home page
class DocHomeForm(forms.Form):
    pendingApp = forms.CharField(label="Pending Appointments ",widget=forms.Select(choices=FRUIT_CHOICES))
    reqApp = forms.CharField(label="Appointment Requests ",widget=forms.Select(choices='Select'))

# Patient Home Form
# No fields as of now
class PatHomeForm(forms.Form):
    i = 1

# Appointment Schedule form
class SchedAppointment(forms.Form):
    dat = forms.DateField(label= "Date", widget= SelectDateWidget)
    time = forms.TimeField(label= "Time")
    docs = forms.ChoiceField(widget= forms.Select, choices= getDocList())

#     Doctor Registration
class docReg(forms.Form):
    uname = forms.CharField(label="Username", max_length= 30)
    pwd = forms.CharField(label=mark_safe("Password "), max_length=30, widget=forms.PasswordInput)
    pwd_conf = forms.CharField(label=mark_safe("Confirm Password "), max_length=30, widget=forms.PasswordInput)
    nam = forms.CharField(label="Name", max_length= 30)
    clinic = forms.CharField(label="Clinic", max_length= 30)
    phone = forms.IntegerField(label="Mobile No (+91)",validators= [MaxValueValidator(9999999999)])
