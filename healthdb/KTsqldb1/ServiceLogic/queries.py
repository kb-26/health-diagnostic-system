from django.db import connection
from KTsqldb1.models import Doctor

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
    for ele in docList:
        print(ele)
    return docList