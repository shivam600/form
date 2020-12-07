from django.db import models

class position(models.Model):
   title=models.CharField(max_length=100)

   def __str__(self):
      return self.title
# Create your models here.
class Destination(models.Model):
   name=models.CharField(max_length=100)
   employee_code=models.CharField(max_length=100)
   phone_no=models.CharField(max_length=15)
   position=models.ForeignKey(position,on_delete=models.CASCADE)
  
     