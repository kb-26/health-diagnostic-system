from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import datetime

from .forms import *


from KTsqldb1.ServiceLogic.queries import *

# Create your views here.

def index(request):
    return HttpResponse("Index of health database")

def homePage(request):
    return render(request, 'index.html')

def patientHome(request):
    return render(request, 'patHome.html')

def patLogin(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            for key in form.cleaned_data:
                print(key)
            uname = form.cleaned_data["uname"]
            pwd = form.cleaned_data["pwd"]
            global res
            res = login(uname, pwd, type= 'P')
            if res:
                global UserName
                UserName = uname
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
            return HttpResponseRedirect('View')

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
                return HttpResponseRedirect("DHome")
            else:
                return render(request, 'docLogin.html', {'form': form})
    else:
        form = loginForm()
    return render(request, 'docLogin.html', {'form':form})

def docHome(request):
    if request.method=='POST':
        return
    form = DocHomeForm()
    
    return render(request, 'docHome.html', {'docname': UserName},{'form':form})

def schedAppointment(request):
    if request.method=='POST':
        return
    form = SchedAppointment()
    return render(request, 'schedAppointment.html', {'form':form})

# calculate the new number of ID
def getNewIDNum(IDList):
    lastID = IDList[-1]
    lastID = lastID[1:]  # Remove starting 'd'
    idNum = int(lastID)  # get the number
    idNum += 1  # and increment it

    newID = str(idNum)
    while (len(newID) < 3):
        newstr = '0' + newID
        newID = newstr
    return newID



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