from django.db import models

# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=70)
    precio = models.IntegerField()
    sabor = models.CharField(max_length=60)
    peso = models.CharField(max_length=8)
    imagen = models.ImageField(upload_to = "productos", null=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)

def __str__(self):
        return self.nombre