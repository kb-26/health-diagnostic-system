from django.db import connection
from KTsqldb1.models import Doctor, DoctorCredentials

def login(uname, pwd, type):    ##type = 'P' for patient, 'D' for doctor
    if(type=='P'):
        with connection.cursor() as cursor:
            cursor.execute("select UserName from KTsqldb1_patientcredentials where UserName = %s", [uname])
            res = cursor.fetchone()
            if not res or not len(res):
                return False
            cursor.execute("select Password from KTsqldb1_patientcredentials where Password = %s", [pwd])
            res = cursor.fetchone()
            if not res or not len(res):
                return False
            return True
    else:
        with connection.cursor() as cursor:
            cursor.execute("select UserName from KTsqldb1_doctorcredentials where UserName = %s", [uname])
            res = cursor.fetchone()
            if not res or not len(res):
                return False
            cursor.execute("select Password from KTsqldb1_doctorcredentials where Password = %s", [pwd])
            res = cursor.fetchone()
            if not res or not len(res):
                return False
            return True

## returns a list of all doctors
def getDocList():
    docList = Doctor.objects.values_list('DoctorID','Name')
    # for ele in docList:
    #     print(ele)
    return docList

#   Return List of docID
def getDocID():
    docIDList = Doctor.objects.values_list('DoctorID',flat= True)
    return list(docIDList)

#   Return list of Doctor Usernames
def getDocUname():
    docUnameList = DoctorCredentials.objects.values_list('UserName', flat= True)
    return list(docUnameList)

#   Called for new Doctor Registration
def docRegistrationQuery(uname, pwd, name, clinic, phone, docID):
    Doctor.objects.create(DoctorID= docID, Name= name, Clinic= clinic, Phone= phone)

    # print(docID)
    docObj = Doctor.objects.get(DoctorID= docID)
    DoctorCredentials.objects.create(UserName= uname, Password= pwd, DoctorID= docObj)
    return
