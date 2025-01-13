from django.db import models

# Create your models here.
class Social(models.Model):
    social_name=models.CharField(max_length=90,default=True)
    moreusedby=models.CharField(max_length=90,default=True)
    social_image=models.ImageField(upload_to="Social",default=True)
    description=models.TextField(default=True)   #for adding deleting same rename steps of migrate shuold be folled
    #charfield can be searched in django model field

      
   
   
class info (models.Model):
    text=models.TextField(null=True)
    output=models.CharField(max_length=90,null=True)
    

class contact(models.Model):
    username=models.CharField(max_length=90,default=True)
    phoneno=models.CharField(max_length=90,default=True)
    email=models.CharField(max_length=90,default=True)
    message=models.TextField(default=True)   #for adding deleting same rename steps of migrate shuold be folled
    #charfield can be sear    