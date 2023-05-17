from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from product.models import fruits


# Create your views here.
def index(request):
    if request.method=='POST':
        dis=request.POST['schitem']
        obj=fruits.objects.filter(name__istartswith=dis)
    else:
        obj=fruits.objects.all()
    print('hi',obj)

    return render(request,"index.html",{'data':obj})


def test(request):
    return render(request,"test.html",{'val':'java'})

def log(request):
    return render(request,"login.html")

def reg(request):
    return render(request,"register.html")

def logsub(request):
    uname=request.POST['uname']
    pname=request.POST['pname']
    user=auth.authenticate(username=uname,password=pname)
    if user:

        auth.login(request,user)
        res=redirect("/")
        res.set_cookie('username',uname)
        return res
    
    return render(request,"login.html",{'val':user})
    

def regsub(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    ename=request.POST['ename']
    uname=request.POST['uname']
    pwd=request.POST['pwd']
    rpwd=request.POST['rpwd']
    if pwd==rpwd:
        if User.objects.filter(username=uname):
            msg="Username Exists..!"
            return render(request,"test2.html",{'val1':msg,'val2':lname,'val3':ename})
        elif User.objects.filter(email=ename):
            msg="Email exists..!"
            return render(request,"test2.html",{'val1':fname,'val2':lname,'val3':msg})
        else:
            user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=ename,password=pwd)  # ORM insertion command
            user.save();
            auth.login(request,user)
            return redirect('/')
    else:
        msg="Password incorrect..!"
        return render(request,"test2.html",{'val1':fname,'val2':lname,'val3':msg})  

def logout(request):
    auth.logout(request)

    lg=redirect("/")
    lg.delete_cookie('username')
    return lg

def feed(request):
    return render(request,'test.html')

def sch(request):
    return render(request,'search.html')

def schsub(request):
    schitem=request.GET['schitem']
    return render(request,'test.html',{'item':schitem})


