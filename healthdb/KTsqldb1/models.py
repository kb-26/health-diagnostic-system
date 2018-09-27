from django.db import models

# Create your models here.
class Doctor(models.Model):
    DoctorID = models.CharField(primary_key= True,max_length= 50)
    Name = models.CharField(max_length=50)
    Clinic = models.CharField(max_length=50)
    Phone = models.CharField(max_length= 10)

class Patient(models.Model):
    PatientID = models.CharField(primary_key= True, max_length= 50)
    Name = models.CharField(max_length=50)
    DOB = models.DateField()
    Age = models.IntegerField(default=0)
    Address = models.CharField(max_length= 200)

class Appointment(models.Model):
    AppointmentID = models.CharField(primary_key= True, max_length= 50)
    AppDate = models.DateField()
    Time = models.TimeField()
    patID = models.ForeignKey(Patient, on_delete= models.CASCADE)
    docID = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Diagnosis(models.Model):
    DiagnosisID = models.CharField(primary_key=True, max_length=50)
    Name = models.CharField(max_length=50)

class Treatment(models.Model):
    TreatmentID = models.CharField(primary_key=True, max_length=50)
    UnitPrice = models.FloatField()
    Duration = models.IntegerField(default= 1)
    Name = models.CharField(max_length=50)
    diagID = models.ForeignKey(Diagnosis, on_delete= models.CASCADE)