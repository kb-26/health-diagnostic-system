# Queries related to Appointment
from KTsqldb1.models import Appointment, Patient, Doctor
from .queries import *

import datetime

# Get current and next year
def getAppointmentYears():
    curr_year = datetime.date.today().year
    return range(curr_year, curr_year+2)

# list of Appointment IDs
def getAppID():
    AppIDList = Appointment.objects.values_list('AppointmentID', flat=True)
    return list(AppIDList)

# Creates new Appointment
def createAppointment(time, date, docID, patID):
    currIDList = getAppID()
    newID = getNewIDNum(currIDList)
    newID = 'a' + newID
    print("New ID = ", newID)

    PatObj = Patient.objects.get(PatientID=patID)
    docObj = Doctor.objects.get(DoctorID=docID)

    newApp = Appointment(AppointmentID= newID, AppDate= date, Time= time, docID=docObj, patID=PatObj)
    newApp.full_clean()
    newApp.save()

    # newApp = Appointment.objects.create(AppointmentID=newID, AppDate=date, Time=time, docID=docObj, patID=PatObj)
    return