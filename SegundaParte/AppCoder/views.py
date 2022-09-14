from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import MiFamilia

# Create your views here.

def Family(request):

    Integrante1 = MiFamilia(nombre = "Carlos", edad = 64)
    Integrante1.save()

    return HttpResponse(f"Un integrante de mi familia es {Integrante1.nombre} y tiene la edad de {Integrante1.edad}")

