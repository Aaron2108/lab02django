from django.shortcuts import render

def index(request):
    context = {
        'titulo': "Ejercicio 1",
    }
    return render(request, 'ejercicio1/formuejer1.html', context)

# Create your views here.
def formulaejer1 (request):
    number1 = int(request.POST.get('number1', 0))  
    number2 = int(request.POST.get('number2', 0))
    operacion = request.POST.get('operacion', '')
    resultado = ''
    if operacion == "+":
     resultado = 'La suma es ' + str(number1 + number2)
    elif operacion == "-":
     resultado = 'La resta es ' + str(number1 - number2)
    elif operacion == "x":
     resultado = 'La multiplicación es ' + str(number1 * number2)

    context = {
        'titulo': "Resultado de la Operacion",
        'resultado': resultado,
    }
    
    return render (request, 'ejercicio1/respuesta1.html', context)