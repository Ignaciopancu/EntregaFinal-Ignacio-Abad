from django.shortcuts import render


def index(request):
    return render(request, "index.html")
# ACA NOSE PORQUE PUSE ESTO PERO LO SAQUE DE LAS DIAPOSITIVAS.