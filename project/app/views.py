from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
# Create your views here.

from django.template import Context,Template


def index(request):
    return render(request,"home/index.html")

def saludo(request):
    return HttpResponse("Hola operadores del Derecho!!")


def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"<h1> {apellido}, {nombre} </h1")


def Formulario(request):
    if request.method == "POST":
          form = forms.AutorForm(request.POST)
          if form.is_valid():
              form.save()
              return  redirect("home.index.html")
    else:
            form = forms.AutorForm()
            context = {"form": form}
            return render(request, "home/Formulario.html", context)