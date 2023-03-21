from django.contrib import admin
from django.urls import path
from home import views as hviews
from members import views as mviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home",hviews.Home,name='home' ),
    path("Signup",mviews.signup,name='Signup' ),
    path("Update",mviews.update,name='Update'),
    # path("managelogin",mviews.managelogin,name='Managelogin'),
    path('hospital/Park_Kalash_Hospital',hviews.parkhospital,name="Hospital"),
    path('hospital/Sawai_Man_Singh_Hospital',hviews.sawai,name="Hospital"),
    path('hospital/AIIMS_Jodhpur',hviews.AIIMS,name="Hospital"),
    path('hospital/Maharao_Bhimsingh_Hospital',hviews.maharao,name="Hospital"),
    path('hospital/Vedanta_Superspeciality_Hospital',hviews.vedanta,name="Hospital"),
    path('hospital/Hari_Ram_Hospital',hviews.hari,name="Hospital"),

    path("managesignup",mviews.managesignup,name='Signup'),
    path("updatingdata",mviews.updatingdata, name="Update")
]