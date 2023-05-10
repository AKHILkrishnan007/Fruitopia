from django.shortcuts import render,redirect
from .models import fruits,comment

# Create your views here.
def details(request):
    iname=request.GET['id']
    obj=fruits.objects.get(id=iname)  #orm command
    return render(request,"about.html",{'data': obj})

def cmt(request):
    imsg=request.GET['cmtmsg']
    iuser=request.GET['user']
    ipro=request.GET['proid']

    obj=comment.objects.create(user=iuser,msg=imsg,pro_id_id=ipro,like=0)
    obj.save()
    return redirect('/product/?id='+ipro)

def like(request):
    return render(request,'test.html')
