from django.db.models.signals import post_save
from .models import *

def create_profile(sender,instance,*args,**kwargs):
    print(sender)
    print(instance)
        # if sender.is_pharmacist == True:
        #     instance.profile = Pharmacist.objects.create()
        #     instance.save()
        # elif sender.is_patient == True:
        #     instance.profile = Patient.objects.create()
        #     instance.save()

# def create_pharmacist_profile(sender,instance,created,*args,**kwargs):
#     if created:
#         instance.profile = Pharmacist.objects.create()
#         instance.save()

post_save.connect(create_profile,sender=User)
# post_save.connect(create_pharmacist_profile,sender=Pharmacist)