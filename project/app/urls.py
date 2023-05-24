from django.urls import path
from app import views


urlpatterns = [
    path("saludar", views.saludo),
    path("nombre/<nombre>/<apellido>/", views.nombre),
    path("Templates", views.probando_template_render),
    path('Formulario', views.Formulario, name='Formulario'),
    ]