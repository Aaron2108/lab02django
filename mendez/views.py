from django.shortcuts import render

def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'mendez/formulario.html', context)
# Create your views here.
def formulario (request):
    context = {
         'titulo': "Respuesta",
         'nombre': request.POST['nombre'],
         'clave': request.POST['password'],
         'educacion': request.POST['educacion'],
         'nacionalidad': request.POST['nacionalidad'],
         'idiomas': request.POST.getlist('idiomas'),
         'correo': request.POST['email'],
         'website': request.POST['sitioweb'],
        }
    return render (request, 'mendez/respuesta.html', context)