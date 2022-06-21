from operator import mod
from statistics import mode
from django.db import models
from django.urls import reverse
import csv
import json
from django.http import JsonResponse

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
    kod         =    models.IntegerField()
    type        =    models.CharField(max_length=30)
    name        =    models.CharField(max_length=120)
    faculty     =    models.CharField(max_length=120)
    department  =  models.CharField(max_length=120)
    point_type  =  models.CharField(max_length=30)
    quota       =    models.IntegerField()
    accepted    =   models.IntegerField()
    min_point   =  models.FloatField()
    max_point   = models.FloatField()

    def __str__(self) -> str:
        return self.department

# return "/university/{}".format(self.id)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'id' : self.id})


def search_uni(request):
    uni_key = request.GET.get('uni')
    results = []
    """if university:
        university_objects = Uni.objects.filter(department=uni_key)
        for i in university_objects:
            results.append([i.name, i.department])"""
    for uni in Uni.objects.all():
        if str(uni_key).lower() in uni.department.lower() or str(uni_key).lower() in uni.name.lower():
            liste =[uni.kod,
                    uni.type,
                    uni.name,
                    uni.faculty,
                    uni.department,
                    uni.point_type,
                    uni.quota,
                    uni.accepted,
                    uni.min_point,
                    uni.max_point]
            results.append(liste)

    return JsonResponse({'status' : 200, 'data' : results}, safe=False, json_dumps_params={'ensure_ascii': False})

"""
with open('data/uni.csv', 'r', encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        # if "Hacettepe".upper() in row[2]:
        #print("Program Kodu : {},Üniversite Türü : {},Üniversite Adı : {},Fakülte/Yüksekokul Adı : {},Program Adı : {}, Puan Türü : {},Genel Kont. : {},Yerleşen : {},En Küçük Puan : {},En Büyük Puan : {}".format(Uni.kod, Uni.type, Uni.name, Uni.faculty, Uni.department, Uni.point_type, Uni.quota, Uni.accepted, Uni.min_point, Uni.max_point))

        university = Uni(int(row[0]),int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        university.save()
"""













