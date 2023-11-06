from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()