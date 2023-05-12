from django.shortcuts import render,redirect
from .models import fruits,comment

# Create your views here.
def details(request):
    iname=request.GET['id']
    obj=fruits.objects.get(id=iname)  #orm command

    if 'recent' in request.session:
       if  iname in request.session['recent']:
           request.session['recent'].remove(iname)
       rct=fruits.objects.filter(id__in=request.session['recent'])
       request.session['recent'].insert(0,iname)
       if len(request.session['recent'])>=5:
           request.session['recent'].pop()
       
       
    else:
        request.session['recent']=[iname]
        rct=[]

    request.session.modified=True
    return render(request,"about.html",{'data': obj,'rec':rct})

def cmt(request):
    imsg=request.GET['cmtmsg']
    iuser=request.GET['user']
    ipro=request.GET['proid']

    obj=comment.objects.create(user=iuser,msg=imsg,pro_id_id=ipro,like=0)
    obj.save()
    return redirect('/product/?id='+ipro)

def like(request):
    proid=request.GET['id']
    
    obj=comment.objects.filter(id=proid)
    l=int(obj[0].like)+1
    obj.update(like=str(l))
    
    return redirect('/product/?id='+str(obj[0].pro_id_id))
