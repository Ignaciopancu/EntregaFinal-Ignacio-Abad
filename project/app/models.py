from django.db import models

# Create your models here.


class Pais(models.Model):
    nombre = models.CharField(max_length=50)


class Usuario(models.Model): #HAY QUE PREGUNTAR SI ESTO PUEDE SE ABOGADO Y 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}" 
    
class Profesion(models.Model):
    profesion = models.CharField(max_length=50)
