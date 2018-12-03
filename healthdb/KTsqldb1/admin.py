from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('HealthDB admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('HealthDB administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')

admin_site = MyAdminSite()

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Diagnosis)
admin.site.register(Treatment)
admin.site.register(PatientCredentials)
admin.site.register(DoctorCredentials)

## Register models with custom admin website

admin_site.register(Patient)
admin_site.register(Doctor)
admin_site.register(Appointment)
admin_site.register(Diagnosis)
admin_site.register(Treatment)
admin_site.register(PatientCredentials)
admin_site.register(DoctorCredentials)