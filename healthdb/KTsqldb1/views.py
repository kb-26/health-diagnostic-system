from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
import sys
sys.path.append('D:\GitHub\health-diagnostic-system\healthdb\KTsqldb1\ServiceLogic')
from queries import login
# Create your views here.

def index(request):
    return HttpResponse("Index of health database")

def homePage(request):
    return render(request, 'index.html')

def patientHome(request):
    return render(request, 'patHome.html')

UserName = ''

def patLogin(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data["uname"]
            pwd = form.cleaned_data["pwd"]
            res = login(uname, pwd, type= 'P')
            if res:
                global UserName
                UserName = uname
                return HttpResponseRedirect("PHome")
            else:
                return render(request, 'patLogin.html', {'form': form})
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

    form = loginForm()
    return render(request, 'docLogin.html', {'form':form})

def docHome(request):
    if request.method=='POST':
        return
    form = DocHomeForm()
    
    return render(request, 'docHome.html', {'docname': UserName},{'form':form})