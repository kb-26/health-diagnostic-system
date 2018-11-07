# Queries related to Appointment
from typing import List

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
    return None

# Return Doctor Names, DoctorID, and Appointment objects for a patient
def getAppointments(patID):
    appObjList = Appointment.objects.filter(patID= patID)
    # appList = list(appList)
    print("Applist")
    apps_DocNames = []
    apps_DocIDs: List[str] = []
    apps_Dates = []
    apps_Times = []
    apps_Status = []
    for app in appObjList:
        # print (app.docID)
        nam = app.docID.Name
        print(nam)
        apps_DocNames.append(nam)
        
        docID = app.docID.DoctorID
        print(docID)
        apps_DocIDs.append(docID)

        dat = app.AppDate
        apps_Dates.append(str(dat))
        print(dat)

        time = app.Time
        apps_Times.append(str(time))
        print(time)

        stat = app.Status
        if stat:
            apps_Status.append("Completed")
        else:
            apps_Status.append("Pending")

    return apps_DocNames, apps_DocIDs, apps_Dates, apps_Times, apps_Status
