from django.shortcuts import render,HttpResponse
from members.models import Signup,Updating,Login
from datetime import time
# Create your views here.
def signup(request):
    return render(request,"signup.html")

def update(request):
    return render(request,"updating.html")
def changevalue(value):
    if value=="":
        return 0
    return int(value)
def managesignup(request):
    if(request.method == 'POST'):
        staffname = request.POST.get("staffname")
        staffpost = request.POST.get("staffpost")
        hospital = request.POST.get("hospital")
        address = request.POST.get("address")
        password = request.POST.get("password")
        signup = Signup(staffname=staffname, staffpost = staffpost, hospital=hospital, address = address, password = password)
        signup.save()
        return render(request,"updating.html")
    else:
        return render(request,"signup.html")

def updatingdata(request):
    if(request.method == "POST"):
        hospitalname = request.POST.get("hospitalname")
        print("Hospital Name =",hospitalname)
        hospitaladdress = request.POST.get("hospitaladdress")
        bloodgroup1 = changevalue(request.POST.get("bloodgroup1"))
        bloodgroup2 = changevalue(request.POST.get("bloodgroup2"))
        bloodgroup3 = changevalue(request.POST.get("bloodgroup3"))
        bloodgroup4 = changevalue(request.POST.get("bloodgroup4"))
        bloodgroup5 = changevalue(request.POST.get("bloodgroup5"))
        bloodgroup6 = changevalue(request.POST.get("bloodgroup6"))
        bloodgroup7 = changevalue(request.POST.get("bloodgroup7"))
        bloodgroup8 = changevalue(request.POST.get("bloodgroup8"))
        ebed = changevalue(request.POST.get("ebed"))
        nbed = changevalue(request.POST.get("nbed"))
        ambulance = changevalue(request.POST.get("ambulance"))
        oxygencylinder = changevalue(request.POST.get("oxygencylinder"))
        oxygenvolume = changevalue(request.POST.get("oxygenvolume"))
        staffname = request.POST.get("staffname")
        staffpost = request.POST.get("staffpost")
        password = request.POST.get("password")
        fpassword = Signup.objects.filter(staffname=staffname,staffpost=staffpost).values('password')
        fpassword= fpassword[0]["password"]
        if(password == fpassword):
            update = Updating(hospitalname=hospitalname, hospitaladdress=hospitaladdress, bloodgroup1=bloodgroup1 , bloodgroup2=bloodgroup2, bloodgroup3=bloodgroup3, bloodgroup4=bloodgroup4, bloodgroup5=bloodgroup5, bloodgroup6=bloodgroup6, bloodgroup7=bloodgroup7, bloodgroup8=bloodgroup8,ebed=ebed, nbed=nbed,
                            ambulance=ambulance, oxygencylinder =oxygencylinder,oxygenvolume=oxygenvolume, staffname=staffname, staffpost=staffpost,password=password )
            update.save()
            return HttpResponse("Updated")
        else:
            return render(request,"updating.html")