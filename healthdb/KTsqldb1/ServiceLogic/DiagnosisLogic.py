from final_v1 import predict_diagnosis
from KTsqldb1.models import Appointment, Patient, Doctor, Diagnosis
import numpy

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
    print(x_vector)
    print(numpy.array([x_vector]).shape)
    # class_num, class_name = predict_diagnosis(x_vector)
    # print(class_name)
    # return class_num, class_name
    class_num = predict_diagnosis(x_vector)
    print(class_num)
    return class_num

# list of Diagnosis IDs
def getDiagID():
    DiagIDList = Diagnosis.objects.values_list('DiagnosisID', flat=True)
    return list(DiagIDList)

# Creates new Diagnosis
def createDiagnosis(name, appID):
    currIDList = getDiagID()
    for ele in currIDList:
        print (ele)

    print (currIDList)
    # assert False
    if len(currIDList) == 0:
        newID = 'g001'      # diagnosis id is 'g'+3 digits
    else:
        newID = getNewIDNum(currIDList)
        newID = 'g' + newID
    print("New ID = ", newID)

# comment
    a = 5
    AppointmentObj = Appointment.objects.get(AppointmentID= appID)
    # docObj = Doctor.objects.get(DoctorID=docID)

    newDiag = Diagnosis(appID=AppointmentObj, Name= name, DiagnosisID= newID)
    newDiag.full_clean()
    newDiag.save()
    # newApp = Appointment.objects.create(AppointmentID=newID, AppDate=date, Time=time, docID=docObj, patID=PatObj)
    return None

