from operator import mod
from statistics import mode
from django.db import models
from django.urls import reverse

"""class Uni(models.Model):
  def __init__(self, kod, type, name, faculty, department, point_type, quota, accepted, min_point, max_point ):

    self.kod  =         kod
    self.type =         type
    self.name =         name
    self.faculty =      faculty
    self.department =   department
    self.point_type =   point_type
    self.quota =        quota
    self.accepted =     accepted
    self.min_point =    min_point
    self.max_point =    max_point"""

class Uni(models.Model):
    kod  =    models.IntegerField()    
    type =    models.CharField(max_length=30)
    name =    models.CharField(max_length=120)
    faculty =    models.CharField(max_length=120)
    department =  models.CharField(max_length=120)
    point_type =  models.CharField(max_length=30)
    quota =    models.IntegerField()       
    accepted =   models.IntegerField()     
    min_point =  models.FloatField()     
    max_point = models.FloatField()      

    def __str__(self) -> str:
        return self.department

# return "/university/{}".format(self.id)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'id' : self.id})
















