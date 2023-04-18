from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth


# Create your views here.
def index(request):
    return render(request,"index.html")

def test(request):
    return render(request,"test.html",{'val':'java'})

def log(request):
    return render(request,"login.html")

def reg(request):
    return render(request,"register.html")

def logsub(request):
    uname=request.GET['uname']
    pname=request.GET['pname']
    user=auth.authenticate(username=uname,password=pname)
    if user:
        auth.login(request,user)
        return redirect("/")
    return render(request,"test.html",{'val':user})
    

def regsub(request):
    fname=request.GET['fname']
    lname=request.GET['lname']
    ename=request.GET['ename']
    pwd=request.GET['pwd']
    rpwd=request.GET['rpwd']
    
    return render(request,"test2.html",{'val1':fname,'val2':lname,'val3':ename})



