from django.shortcuts import render
from .models import Shooter,Rogelite,Soulslike

# Create your views here.
def shooter_list(request):
    shooter=Shooter.objects.all()
    return render(request, 'Juegos/shooter_list.html',{'shooter_mostrar':shooter})

def rogelite_list(request):
    rogelite=Rogelite.objects.all()
    return render(request, 'Juegos/rogelite_list.html',{'rogelite_mostrar':rogelite})

def soulslike_list(request):
    soulslike=Soulslike.objects.all()
    return render(request, 'Juegos/soulslike_list.html',{'soulslike_mostrar':soulslike})