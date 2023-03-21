from django.db import models
from datetime import datetime
# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

class Signup(models.Model):
    staffname = models.CharField(max_length=50)
    staffpost = models.CharField(max_length=50)
    hospital = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=25)
    date = models.DateTimeField(default=datetime.today())
    
class Updating(models.Model):
    hospitalname = models.CharField(max_length=100)
    hospitaladdress = models.CharField(max_length=100)
    bloodgroup1 = models.IntegerField(default=0)
    bloodgroup2 = models.IntegerField(default=0)
    bloodgroup3 = models.IntegerField(default=0)
    bloodgroup4 = models.IntegerField(default=0)
    bloodgroup5 = models.IntegerField(default=0)
    bloodgroup6 = models.IntegerField(default=0)
    bloodgroup7 = models.IntegerField(default=0)
    bloodgroup8 = models.IntegerField(default=0)
    ebed = models.IntegerField(default=0)
    nbed = models.IntegerField(default=0)
    ambulance = models.IntegerField(default=0)
    oxygencylinder = models.IntegerField(default=0)
    oxygenvolume = models.IntegerField(default=0)
    staffname = models.CharField(max_length=100)
    staffpost = models.CharField(max_length=100)
    password = models.CharField(max_length=25)
    image = models.ImageField(default=0,upload_to="static")
    address_url = models.URLField(max_length=1000)
    date = models.DateTimeField(default=datetime.today())