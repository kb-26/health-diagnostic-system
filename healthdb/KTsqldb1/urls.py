from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="Index"),
    path('home', views.homePage, name="HomeScreen"),
    path('plogin', views.patLogin, name="PatientLogin"),
    path('dlogin', views.docLogin, name="DoctorLogin"),
    path('PHome', views.patHome, name= "PatientHome"),
    path('DHome', views.docHome, name= "ome"),
    path('Schedule', views.schedAppointment, name= "ScheduleAppointments"),
    path('dRegister', views.docRegistration, name= "DoctorRegistration")
]