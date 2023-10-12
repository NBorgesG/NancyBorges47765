from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Maquillaje(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre}    Color: {self.color}    Precio: {self.precio} Descripción: {self.descripcion}"
    nombre = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to="imgProductos/maquillajes", null=True, blank=True)
    color = models.CharField(max_length=10)
    precio = models.IntegerField() 
    descripcion = models.TextField(max_length=1000)
    autor = models.CharField(max_length=50)

class Accesorio(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre}    Color: {self.color}    Precio: {self.precio} Descripción: {self.descripcion}"
    nombre = models.CharField(max_length=40, default='false')
    imagen = models.ImageField(upload_to="imgProductos/accesorios", null=True, blank=True)
    color = models.CharField(max_length=10)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=1000)
    autor = models.CharField(max_length=50)

class CremasFaciales(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre}  Precio: {self.precio} Descripción: {self.descripcion}"
    nombre = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to="imgProductos/cremasFaciales", null=True, blank=True)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=1000) 
    autor = models.CharField(max_length=50)

class CremasCorporales(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre}     Precio: {self.precio} Descripción: {self.descripcion}"
    nombre = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to="imgProductos/cremasCorporales", null=True, blank=True)
    precio = models.IntegerField() 
    descripcion = models.TextField(max_length=1000)
    autor = models.CharField(max_length=50)

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)