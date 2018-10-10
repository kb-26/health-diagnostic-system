from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import loginForm
import sys
sys.path.append('D:\Documents\PycharmProjects\WebProject2\healthdb\KTsqldb1\ServiceLogic')
from queries import login
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
            uname = form.cleaned_data["uname"]
            pwd = form.cleaned_data["pwd"]
            res = login(uname, pwd, type= 'P')
            if res:
                return HttpResponseRedirect("/pLogin/")
            else:
                return render(request, 'patLogin.html', {'form': form})
    form = loginForm()
    return render(request, 'patLogin.html', {'form':form})

def docLogin(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data["uname"]
            pwd = form.cleaned_data["pwd"]
            res = login(uname, pwd, type= 'D')
            if res:
                return HttpResponseRedirect("/dLogin/")
            else:
                return render(request, 'docLogin.html', {'form': form})
    form = loginForm()
    return render(request, 'docLogin.html', {'form':form})