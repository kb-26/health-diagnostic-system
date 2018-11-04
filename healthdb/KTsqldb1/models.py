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


# IMPORTANT :
#           Appointment foreign key definition is different from that specified here
class Appointment(models.Model):
    AppointmentID = models.CharField(primary_key= True, max_length= 50)
    AppDate = models.DateField()
    Time = models.TimeField()
    patID = models.ForeignKey(Patient, on_delete= models.CASCADE)
    docID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Status = models.BooleanField(default= False)

    class Meta:
        unique_together = (("AppDate", "Time", "docID"))
        # unique_together("")

class Diagnosis(models.Model):
    DiagnosisID = models.CharField(primary_key=True, max_length=50)
    Name = models.CharField(max_length=45)
    appID = models.ForeignKey(Appointment, on_delete=models.CASCADE)

class Treatment(models.Model):
    TreatmentID = models.CharField(primary_key=True, max_length=50)
    UnitPrice = models.FloatField()
    Duration = models.IntegerField(default= 1)
    Name = models.CharField(max_length=50)
    diagID = models.ForeignKey(Diagnosis, on_delete= models.CASCADE)

class PatientCredentials(models.Model):
    UserName = models.CharField(primary_key=True, max_length=50)
    Password = models.CharField( max_length=50)
    PatientID = models.ForeignKey(Patient, on_delete= models.CASCADE, default="p001")

class DoctorCredentials(models.Model):
    UserName = models.CharField(primary_key=True, max_length=50)
    Password = models.CharField( max_length=50)
    DoctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE, default= "d001")