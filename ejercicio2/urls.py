from django.urls import path

from . import views

app_name = 'ejercicio2'

urlpatterns = [
    path('', views.index, name='index'),
    path('formuejer2', views.formulaejer2, name='formuejer2'),
]