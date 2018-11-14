from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ValidationError

import datetime

from .forms import *


from KTsqldb1.ServiceLogic.queries import *
from KTsqldb1.ServiceLogic.DoctorLogic import *
from KTsqldb1.ServiceLogic.AppointmentLogic import *
from KTsqldb1.ServiceLogic.TreatmentLogic import *
from KTsqldb1.ServiceLogic.DiagnosisLogic import *

# Create your views here.

def index(request):
    if request.method == 'POST':
        if 'patreg' in request.POST:
            return HttpResponseRedirect('pRegister')
        if 'docreg' in request.POST:
            return HttpResponseRedirect('dRegister')
        if 'patlog' in request.POST:
            return HttpResponseRedirect('plogin')
        if 'doclog' in request.POST:
            return HttpResponseRedirect('dlogin')

    return render(request, 'TestHomePage.html')

def homePage(request):
    return render(request, 'index.html')

def patLogin(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            # for key in form.cleaned_data:
            #     print(key)
            uname = form.cleaned_data["uname"]
            pwd = form.cleaned_data["pwd"]
            global res
            res = login(uname, pwd, type= 'P')
            if res:
                global UserName
                UserName = uname
                global ID
                ID = getpatientID(uname)
                # print(request.session.session_key)
                global SessionKey
                SessionKey = request.session.session_key

                print("SessionKey = ", SessionKey)
                request.session["Username"] = uname
                return HttpResponseRedirect("PHome")
            # else:
            #     form.clean()
            #     for key in form.cleaned_data:
            #         print(key)
    else:
        form = loginForm()
    return render(request, 'patLogin.html', {'form':form})


def patHome(request):
    if request.method=='POST':
        if 'sched' in request.POST:
            return HttpResponseRedirect('Schedule')
        else:
            return HttpResponseRedirect('viewAppointments')

    return render(request, 'patHome.html', {'patname': UserName})



def docLogin(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data["uname"]
            pwd = form.cleaned_data["pwd"]
            res = login(uname, pwd, type= 'D')
            if res:
                global UserName
                UserName = uname
                global ID
                ID = getdoctorID(uname)
                # global SessionKey
                # SessionKey = request.session.session_key
                # print("SessionKey = ", SessionKey)
                # request.session["Username"] = uname
                # request.session["ID"] = getdoctorID(uname)
                # print("ID = ", request.session["ID"])
                return HttpResponseRedirect("DHome")
            else:
                return render(request, 'docLogin.html', {'form': form})
    else:
        form = loginForm()
    return render(request, 'docLogin.html', {'form':form})

def docHome(request):


    if request.method=='POST':
        form = DocHomeForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("treatment")
    # data = {'appointments':getAppointmentDisplay_Doctor()}
    form = DocHomeForm()
    # print("Id is still : ", request.session['ID'])
    # form.data['appointments'].choices = getAppointmentDisplay_Doctor(request.session['ID'])
    return render(request,
                  'docHome.html',
                  {
                      'docname': UserName,
                      'form':form,
                  }, )

def diagnosisDisplayPage(request):
    if(request.method == 'POST'):
        return HttpResponseRedirect("DHome")
    else:
        class_num = int(request.session["class_num"])
        return render(request, 'diagnosisDisplay.html',
                      {'diseaseNum': class_num,
                       'diseaseNam': ''})  # replace with 'diseaseNam' : 'class_name'

def treatmentPage(request):
    if request.method == 'POST':
        form = treatmentForm(request.POST)
        if form.is_valid():

            argList = []
            for key in form.cleaned_data:
                print(key, ':', form.cleaned_data.get(key))
                # argList.append(form.cleaned_data.get(key))
            symptomsList = form.cleaned_data.get('symptoms_list')
            class_num = callPredict(symptomsList)
            request.session["class_num"] = str(class_num)

            argList.append("Disease number: "+ str(class_num)) #TODO: replace class_num with the class name

            # # TODO: value needs to be altered using javascript
            appID = "a001"
            argList.append(appID)  # TODO: Change this to comply with the above

            print("Arg List")
            for ele in argList:
                print(ele)

            #
            try:
                createDiagnosis(*argList)
            except ValidationError:
                messages.error(request, "Diagnosis could not be generated, please contact your system admin")
                return HttpResponseRedirect('treatment')
            #
            messages.success(request, "Diagnosis Generated")

            updateStatus(appID) # Update the appointment and change the status

            return HttpResponseRedirect('Diagnosis')

    else:
        form = treatmentForm()
    return render(request, 'treatment.html', {'form':form})


def viewAppointment(request):

    Dlist, DocIDList, AppDateList, AppTimeList, AppStatusList = getAppointments('p001')

    # for gp in Dlist:
    #     print(gp)

    print("In View : ")
    for id in DocIDList:
        print(id)
    for status in AppStatusList:
        print(status)

    return render(request, 'viewAppointment.html', {'docDisplayNameList':Dlist, 'docDisplayIDList':DocIDList,
                                                    'AppDateList':AppDateList ,'AppTimeList' : AppTimeList, 'AppStatusList':AppStatusList,})

def schedAppointment(request):
    if request.method=='POST':
        # PERFORM VALIDATIONS FOR UNIQUE CONSTRAINTS
        form = SchedAppointment(request.POST)
        if form.is_valid():
            # Validate the time field
            time = request.POST.get('time')
            print("time value from POST = ", time)

            argList=[]
            argList.append(time)
            for key in form.cleaned_data:
                print(key, ':', form.cleaned_data.get(key))
                argList.append(form.cleaned_data.get(key))

            #TODO: Write code to add patient ID from SESSION
            argList.append("p002") # TODO: Change this to comply with the above

            print("Arg List")
            for ele in argList:
                print(ele)

            try:
                createAppointment(*argList)
            except ValidationError:
                messages.error(request, "Appointment could not be scheduled, please choose another time")
                return HttpResponseRedirect('Schedule')

            messages.success(request, "Appointment Scheduled")
            return HttpResponseRedirect('Schedule')

    else:
        form = SchedAppointment()
    return render(request, 'schedAppointment.html', {'form':form})

# Doctor Registration
def docRegistration(request):
    if request.method == 'POST':
        form = docReg(request.POST)
        if form.is_valid():

            currIDList = getDocID()
            newID = getNewIDNum(currIDList)
            newID = 'd' + newID
            print("New ID = ", newID)

            argList = []
            cd = form.cleaned_data
            for key in cd:
                print(key, ':', cd.get(key))
                if key != 'pwd_conf':    # not sure if there are any other special values
                    argList.append(cd.get(key))

            argList.append(newID)

            for arg in argList:
                print(arg)

            # Insert new record in table
            docRegistrationQuery(*argList)      # Comment out this line when testing to prevent database writes
            print("Success message")
            messages.success(request, 'Registration Successful')
            return HttpResponseRedirect("dRegister")
    else:
        form = docReg()
    return render(request, 'docRegistration.html', {'form' : form})

# Patient Registration
def patRegistration(request):
    if request.method == 'POST':
        form = patReg(request.POST)
        if form.is_valid():

            currIDList = getPatID()
            newID = getNewIDNum(currIDList)
            newID = 'p' + newID
            print("New ID = ", newID)

            # dob_post = request.POST.
            argList = []
            for key in form.cleaned_data:
                print(key, ':', form.cleaned_data.get(key))
                if key != 'pwd_conf':    # not sure if there are any other special values
                    argList.append(form.cleaned_data.get(key))


            argList.append(newID)

            for arg in argList:
                print(arg)

            # Insert new record in table
            patRegistrationQuery(*argList)



            # print("Success message")
            messages.success(request, 'Registration Successful')
            return HttpResponseRedirect("pRegister")
    else:
        form = patReg()
    return render(request, 'patRegistration.html', {'form' : form})
