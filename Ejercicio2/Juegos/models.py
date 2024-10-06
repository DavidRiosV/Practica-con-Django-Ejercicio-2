from django.conf import settings
from django.db import models
from django.utils import timezone

class Shooter(models.Model):
    nombre = models.CharField(max_length=200)
    creador = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Rogelite(models.Model):
    nombre = models.CharField(max_length=200)
    creador = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Soulslike(models.Model):
    nombre = models.CharField(max_length=200)
    creador = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre