from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

class Stock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)

class Compra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()