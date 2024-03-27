from django.urls import path

from . import views

app_name = 'ejercicio1'

urlpatterns = [
    path('', views.index, name='index'),
    path('formuejer1', views.formulaejer1, name='formuejer1'),
]