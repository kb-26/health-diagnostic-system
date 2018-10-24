from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .constants import res, UserName
import sys

from KTsqldb1.ServiceLogic.queries import login
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

def docRegistration(request):
    if request.method == 'POST':
        form = docReg(request.POST)
        if form.is_valid():
            for key, value in request.POST.items():
                print(key, ':', value)
    else:
        form = docReg()
    return render(request, 'docRegistration.html', {'form' : form})