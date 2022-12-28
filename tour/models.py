from http.client import ImproperConnectionState
from django.db import models
from django.db.models import Model
from django.urls import reverse

# Create your models here.

class TourType(Model):
    type = models.TextField()
    def __str__(self) -> str:
        return self.type

class Tour(Model):
    type_tour = models.ForeignKey(TourType, on_delete=models.CASCADE, verbose_name='Тип тура')
    price = models.FloatField(verbose_name='Цена')
    place = models.TextField(verbose_name='Место')
    date = models.DateField(verbose_name='Дата')
    def get_absolute_url(self):
        return reverse("home")
