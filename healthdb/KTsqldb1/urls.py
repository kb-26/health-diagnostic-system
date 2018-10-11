from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="Index"),
    path('home', views.homePage, name="HomeScreen"),
    path('plogin', views.patLogin, name="PatientLogin"),
    ##path('patWelcome', views.patientHome, name="PatWelcome"),
    path('dlogin', views.docLogin, name="DoctorLogin")
]