from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def Entregable (request):
    Fecha = datetime.now()
    return HttpResponse(f"Mi primer MTV - Maria Florencia Angulo. Fecha {Fecha}")
 
def Tutor(request, nombre):
    return HttpResponse(f"El tutor que corrige este trabajo se llama: {nombre}")

def Familia(request):
    madre="Alicia"
    padre="Carlos"
    hermano="Gabriel"
    perro="Oliver"
    lista=[66, 64, 30, 7]

    diccionario={"mum":madre, "dad":padre, "bro":hermano, "dog":perro, "ages":lista}

    miHtml = open("C:/Users/mar_f/Desktop/Entregable/MTVFlorencia/MTVFlorencia/Templates/Template1.html")
    Plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context(diccionario)
    documento = Plantilla.render(miContexto)
    return HttpResponse(documento)



