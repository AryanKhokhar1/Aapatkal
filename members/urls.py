from django.contrib import admin
from django.urls import path
from members import views as mviews
from home import views as hviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',hviews.Home,name="Home"),
    path("Signup",mviews.signup,name='Signup'),
    path("Update",mviews.update,name='Update'),
    path('hospital/Park Kalash Hospital',hviews.parkhospital,name="Hospital"),
    # path("managelogin",mviews.managelogin,name="ManageLogin"),
    path("managesignup",mviews.managesignup,name="ManageSignup"),
    path("updatingdata",mviews.updatingdata, name="ManageUpdate")
]