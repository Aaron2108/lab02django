from django.shortcuts import render
def index(request):
    context = {
        'titulo': "Ejercicio 2",
    }
    return render(request, 'ejercicio2/formuejer2.html', context)
# Create your views here.
def formulaejer2 (request):
    diametro = float(request.POST.get('diametro', ''))  
    altura = float(request.POST.get('altura', ''))
    radio = diametro/2
    pi= 3.14159
    operacion = pi * (radio ** 2) * altura
    resultado = 'El volumen del cilindro es de '+ str(operacion)
    context = {
        'titulo': "Resultado de la Operacion 2",
        'resultado': resultado,
    }
    
    return render (request, 'ejercicio2/respuesta2.html', context)