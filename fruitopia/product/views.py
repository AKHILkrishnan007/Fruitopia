from django.shortcuts import render
from .models import fruits

# Create your views here.
def details(request):
    iname=request.GET['id']
    obj=fruits.objects.get(id=iname)  #orm command
    return render(request,"about.html",{'data': obj})

def cmt(request):
    return render(request,'test.html')

def like(request):
    return render(request,'test.html')
