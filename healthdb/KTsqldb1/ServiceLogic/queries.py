from django.db import connection


# calculate the new number of ID
def getNewIDNum(IDList):
    lastID = IDList[-1]
    lastID = lastID[1:]  # Remove starting character
    idNum = int(lastID)  # get the number
    idNum += 1  # and increment it

    newID = str(idNum)
    while (len(newID) < 3):
        newstr = '0' + newID
        newID = newstr
    return newID

# login function
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
