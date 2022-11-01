from django.db import models

# Create your models here.

class place(models.Model):
   name= models.CharField(max_length=100)
   img= models.ImageField(upload_to='picture')
   desc= models.TextField()
   price= models.IntegerField()
   offer= models.BooleanField(default=False)

# class date(models.Model):
#    day = models.IntegerField()
#    month= models.CharField(max_length=100)
#    img= models.ImageField(upload_to='picture')
#    desc= models.TextField()
class date():
   id:int
   day:int
   month:str
   img:str
   desc:str

