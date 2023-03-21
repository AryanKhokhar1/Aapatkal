from django.shortcuts import HttpResponse,render
from members.models import Login,Signup,Updating
# Create your views here.
def Home(request):
    # fstaffname = Signup.objects.filter(staffname = 'Aryan').values_list()

    # fstaffname = Signup.objects.filter(staffname='abcd').values('password')
    # fstaffname = fstaffname.password()
    # context = {
    # 'staffname': fstaffname
    # }
    # return render(request,"signup.html")


    # fimage = Updating.objects.filter(staffname="Shambhavi").values("image")
    # context = {
    #     'image':fimage
    # }
    return render(request,"index.html")
    
def parkhospital(request):
    detail = Updating.objects.filter(hospitalname= "Park Kalash Hospital").values()
    context = {
        'detail':detail[0],
        'imageurl':"https://lh3.googleusercontent.com/p/AF1QipPCG46_jJVLGKzsKeVjHTjY9xoJDxJGrbghRU-g=w1080-h608-p-no-v0"
    }

    return render(request,"hospital.html",context)
def sawai(request):
    detail = Updating.objects.filter(hospitalname= "Sawai Man Sing Hospital").values()
    print(detail)
    context = {
        'detail':detail[0],
        'imageurl': "https://www.jaipurstuff.com/wp-content/uploads/2019/04/SMS-Hospital.jpg"
    }
    return render(request,"hospital.html",context)

def AIIMS(request):
    detail = Updating.objects.filter(hospitalname= "AIIMS Jodhpur Hospital").values()
    print(detail)
    context = {
        'detail':detail[0],
        'imageurl': "https://qph.cf2.quoracdn.net/main-qimg-ad514f8f4b41a38cc351cbddba9ced86-pjlq"
    }
    return render(request,"hospital.html",context)

def maharao(request):
    detail = Updating.objects.filter(hospitalname= "Maharao Bhimsingh Hospital").values()
    print(detail)
    context = {
        'detail':detail[0],
        'imageurl': "https://images.bhaskarassets.com/thumb/1800x1800/web2images/521/2020/04/20/newldw10_1587380153.jpg"
    }
    return render(request,"hospital.html",context)

def vedanta(request):
    detail = Updating.objects.filter(hospitalname= "Vedanta Superspeciality Hospital").values()
    print(detail)
    context = {
        'detail':detail[0],
        'imageurl': "http://www.kayawell.com/Data/Practice//179a5905-c1b1-4643-b18a-b2b7031c19b1.jpg"
    }
    return render(request,"hospital.html",context)

def hari(request):
    detail = Updating.objects.filter(hospitalname= "Hari Ram Hospital").values()
    print(detail)
    context = {
        'detail':detail[0],
        'imageurl':'https://doctorlistingingestionpr.blob.core.windows.net/doctorprofilepic/1665224017804_HospitalProfileImage_fef858eb-1149-40eb-ae2e-3fd7ef107d5c.png'
    }
    return render(request,"hospital.html",context)