from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class Entrada(models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.TextField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='static/img/')

class Curso(models.Model):
    titulo = models.CharField(max_length=40)
    fecha = models.DateField()
    precio = models.IntegerField()
    cupos = models.IntegerField(default=20)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='static/img/')
