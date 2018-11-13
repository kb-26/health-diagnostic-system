from final_v1 import predict_diagnosis
from KTsqldb1.models import Appointment, Patient, Doctor, Diagnosis
from .queries import *

def getOneHotVector(valuelist):
    onehot = []

    for i in range(132):
        if str(i) in valuelist:
            onehot.append(1)
        else:
            onehot.append(0)
    return onehot

def callPredict(x_vector):
    x_vector = getOneHotVector(x_vector)
    class_num, class_name = predict_diagnosis(x_vector)
    print(class_name)
    return class_num, class_name

# list of Diagnosis IDs
def getDiagID():
    DiagIDList = Diagnosis.objects.values_list('DiagnosisID', flat=True)
    return list(DiagIDList)

# Creates new Diagnosis
def createDiagnosis(name, appID):
    currIDList = getDiagID()
    if currIDList is None:
        newID = 'diag1'
    else:
        newID = getNewIDNum(currIDList)
        newID = 'diag' + newID
    print("New ID = ", newID)

    AppointmentObj = Appointment.objects.get(AppointmentID= appID)
    # docObj = Doctor.objects.get(DoctorID=docID)

    newDiag = Appointment(AppointmentID= AppointmentObj, Name= name, DiagnosisID= newID)
    newDiag.full_clean()
    newDiag.save()
    # newApp = Appointment.objects.create(AppointmentID=newID, AppDate=date, Time=time, docID=docObj, patID=PatObj)
    return None

