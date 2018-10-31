from django import forms
import datetime
from django.utils.safestring import mark_safe
from django.forms.widgets import SelectDateWidget
from django.core.validators import MaxValueValidator


from KTsqldb1.ServiceLogic.queries import getDocList, login, getDocUname
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

    def clean(self):  # Throw invalid password exception
        cd = self.cleaned_data
        #   Check for login in both Patient and Doctor tables
        if not login(cd.get('uname'),cd.get('pwd'), type= 'P') and not login(cd.get('uname'),cd.get('pwd'), type= 'D'):
            self.add_error('pwd','Invalid Username or password')
        return cd


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
    pwd_conf = forms.CharField(label=mark_safe("Confirm Password "), max_length=30, widget=forms.PasswordInput,
                               error_messages={'required':'Please Confirm Password',})
    nam = forms.CharField(label="Name", max_length= 30)
    clinic = forms.CharField(label="Clinic", max_length= 30)
    phone = forms.IntegerField(label="Mobile No (+91)",validators= [MaxValueValidator(9999999999)])

    def clean(self):
        cd = self.cleaned_data
        if cd.get('uname') in getDocUname():
            self.add_error('uname', 'Username already taken')
        if cd.get('pwd') != cd.get('pwd_conf'):
            self.add_error('pwd_conf','passwords do not match')
        # if len(cd.get('phone')) != 10:
        #     self.add_error('phone', 'Phone number length should be 10 digits')
        return cd
