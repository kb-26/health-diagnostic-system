# Doctor related queries
from KTsqldb1.models import Doctor, DoctorCredentials

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
def docRegistrationQuery(uname, pwd, name, clinic, phone, docID) :
    Doctor.objects.create(DoctorID= docID, Name= name, Clinic= clinic, Phone= phone)

    # print(docID)
    docObj = Doctor.objects.get(DoctorID= docID)
    DoctorCredentials.objects.create(UserName= uname, Password= pwd, DoctorID= docObj)
    return
