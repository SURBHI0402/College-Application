from django.shortcuts import render
from .models import DeptModel,StuModel
from .forms import DeptForm,StuForm
def home(request):
    return render(request,"home.html")


def dept(request):
    data=DeptModel.objects.all()
    return render(request,"dept.html",{"data":data})

def adddept(request):
    if request.method=="POST":
        data=DeptForm(request.POST)
        if data.is_valid():
            data.save()
            msg="dept created"
            fm=DeptForm()
            return render(request,"adddept.html",{"fm":fm,"mgs":msg})
        else:
            msg="check errors"
            return render(request,"adddept.html",{"fm":data,"msg":msg})
    else:
        fm=DeptForm()
        return render(request,"adddept.html",{"fm":fm})
    
def remdept(request,id):
    de=DeptModel.objects.get(did=id)
    de.delete()
    return redirect("dept")

def stu(request):
    data=StuModel.objects.all()
    return render(request,"stu.html",{"data":data})

def addstu(request):
    if request.method=="POST":
        data=StuForm(request.POST)
        if data.is_valid():
            data.save()
            msg="student created"
            fm=StuForm()
            return render(request,"addstu.html",{"fm":fm,"msg":msg})
        else:
            msg="check errors"
            return render(request,"addstu.html",{"fm":data,"msg":msg})
    else:
        fm=StuForm()
        return render(request,"addstu.html",{"fm":fm})    
def remstu(request,id):
    s=StuModel.objects.get(rno=id)
    s.delete()
    return redirect("stu")
    
