from django.db import models
# import math
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date

# Create your models here.

class User(AbstractUser):
    # @property
    # def is_pharmacist(self):
    #     if hasattr(self, 'pharmacist'):
    #         return True
    #     return False

    # @property
    # def is_patient(self):
    #     if hasattr(self, 'patient'):
    #         return True
    #     return False
    is_patient = models.BooleanField(default=False)
    is_pharmacist = models.BooleanField(default=False)



class Pharmacist(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    gender = models.CharField(max_length=300)
    email = models.EmailField(null=True)
    DOB = models.DateField(null=True)
    picture = models.ImageField(upload_to='profile_pic')
    # user =  models.OneToOneField(User,on_delete=models.CASCADE)

    def __Str__(self):
        return self.first_name+' '+self.last_name


class Pharmacy(models.Model):
    name = models.CharField(max_length=500)
    Description = models.TextField()
    owner = models.OneToOneField(Pharmacist,on_delete=models.CASCADE)
    longitude = models.IntegerField()
    latitude = models.IntegerField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=750)
    description = models.TextField()
    available_quantity = models.IntegerField()
    exp_date = models.DateField()
    add_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    unit_price = models.IntegerField()
    pharmacy = models.ForeignKey(Pharmacy,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Patient(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    DOB = models.DateField(null=True)
    gender = models.CharField(max_length=500)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    longitude =models.IntegerField(null=True)
    latitude = models.IntegerField(null=True)
    # user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name+' '+self.last_name


# class Cart(models.Model):
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     price = models.IntegerField()
#     quantity = models.IntegerField()
    
    



def create_profile(sender,instance,created,*args,**kwargs):
    print(sender)
    print(instance)
    if created:
        if instance.is_pharmacist:
            instance.profile = Pharmacist.objects.create()
            instance.save()
        elif instance.is_patient == True:
            instance.profile = Patient.objects.create()
            instance.save()

# def create_pharmacist_profile(sender,instance,created,*args,**kwargs):
#     if created:
#         instance.profile = Pharmacist.objects.create()
#         instance.save()

post_save.connect(create_profile,sender=User)
# post_save.connect(create_pharmacist_profile,sender=Pharmacist)