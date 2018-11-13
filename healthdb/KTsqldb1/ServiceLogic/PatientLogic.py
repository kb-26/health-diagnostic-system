# Patient Related Queries and Functions
#   Return list of Doctor Usernames
from KTsqldb1.models import Patient, PatientCredentials
import datetime


# Fills valid years in YEARS list for Date Of Birth Field
# Current Year - 110
def getDOBYears():
    init_year = datetime.date.today().year - 120
    YEARS = range(init_year, datetime.date.today().year+1)
    return YEARS


def getPatUname():
    patUnameList = PatientCredentials.objects.values_list('UserName', flat= True)
    return list(patUnameList)

#   Return List of patID
def getPatID():
    patIDList = Patient.objects.values_list('PatientID',flat= True)
    return list(patIDList)

#   Called for new Patient Registration
def patRegistrationQuery(uname, pwd, name, address, dob, patID):
    age = datetime.date.today() - dob
    print("age = ",age)
    print("age in days = ", int(age.days))
    Patient.objects.create(PatientID= patID, Name= name, Address=address, DOB=dob, Age= int(age.days))

    # print(docID)
    PatObj = Patient.objects.get(PatientID= patID)
    PatientCredentials.objects.create(UserName= uname, Password= pwd, PatientID= PatObj)
    return

# return PatID of a username
def getpatientID(uname):
    credObj = PatientCredentials.objects.get(UserName= uname)
    return credObj.PatientID.PatientID