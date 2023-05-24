from django.db import models

# Create your models here.
class Persona(models.Model):
    #llave primaria
    id = models.AutoField(primary_key=True) #se autoincrementa
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=120)
    correo = models.CharField(max_length=200)
