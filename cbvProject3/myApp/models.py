from django.db import models
from django.urls import reverse

# Create your models here.
class HOD(models.Model):
     name=models.CharField(max_length=30)
     no=models.IntegerField()
     exp=models.IntegerField()
     sal=models.IntegerField()
     def get_absolute_url(self):
         return reverse('hoddetail',kwargs={'pk':self.pk})

