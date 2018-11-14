# Queries related to Appointment
from typing import List
from django.contrib.sessions.models import Session
from KTsqldb1.models import Appointment, Patient, Doctor
from .queries import *
from KTsqldb1.constants import *

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

# Return Doctor Names, DoctorID, and other appointment details for a patient
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

# Return Appointment ID, Patient Names, PatientID, and other appointment details for a doctor
def getAppointments_Doctor(docID):
    appObjList = Appointment.objects.filter(docID= docID)
    # print("Applist_Doctors")
    apps_appIDs = []
    apps_PatNames = []
    apps_PatIDs: List[str] = []
    apps_Dates = []
    apps_Times = []
    apps_Status = []

    for app in appObjList:
        # print (app.docID)
        appID = app.AppointmentID
        apps_appIDs.append(appID)
        # print(appID)

        nam = app.patID.Name
        # print(nam)
        apps_PatNames.append(nam)

        patID = app.patID.PatientID
        # print(patID)
        apps_PatIDs.append(patID)

        dat = app.AppDate
        apps_Dates.append(str(dat))
        # print(dat)

        time = app.Time
        apps_Times.append(str(time))
        # print(time)

        stat = app.Status
        if stat:
            apps_Status.append("Completed")
        else:
            apps_Status.append("Pending")

    return apps_appIDs, apps_PatNames, apps_PatIDs, apps_Dates, apps_Times, apps_Status

# Gets appointment details for doctor in format for Radio Button
def getAppointmentDisplay_Doctor(docID):
    # global SessionKey
    # if SessionKey == '':
    #     return []
    # s = Session.objects.get(pk=SessionKey)
    # if s is None:
    #     return []
    # docID = s.get_decoded().get('ID')
    print("ID = ",docID)
    apps_appIDs, apps_PatNames, apps_PatIDs, apps_Dates, apps_Times, apps_Status = getAppointments_Doctor(docID)

    # Get suitable format for the Radio Button Display
    displayList = []
    for patName, dat, time in zip(apps_PatNames, apps_Dates, apps_Times):
        displayList.append("Appointment with " + patName + ", (dated " + dat + ") at " + time)

    for ele in displayList:
        print(ele)
    doc_appList = zip(apps_appIDs, displayList)
    return doc_appList

# update the status of an appointment that has been successfully treated
def updateStatus(appid):
    appointments = Appointment.objects.filter(AppointmentID= appid) # get the appointment object, wrapped by a list
    for app in appointments:
        app.Status = True
        app.full_clean()
        app.save()
        break                   # Loop should run only once

    return True # success
