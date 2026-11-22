from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

#Una de las cosas que agrege en los models fue el "on_delete=models."protect" <- este protect es mas que nada que si un dato esta relacionado con otro no lo puede eliminar, teniendo mayor gestion y control con el tema de cancelaciones u otras cosas. tip pro sioke xd

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator])
    activo = models.BooleanField(default=True)

class Pedido(models.Model):
    ESTADOS_PEDIDO = [
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    ]

    ESTADOS_PREPARACION = [
        ('pendiente', 'Pendiente'),
        ('en_preparacion', 'En preparación'),
        ('preparado', 'Preparado'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )

    fecha_servicio = models.DateField()
    fecha_hora_creacion = models.DateTimeField(auto_now_add=True)

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS_PEDIDO,
        default='confirmado'
    )

    estado_preparacion = models.CharField(
        max_length=20,
        choices=ESTADOS_PREPARACION,
        default='pendiente'
    )


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, related_name='detalles')
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=['pedido', 'producto'],name='producto_unico_por_pedido')]

class EstadoPreparacion(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, related_name='historial_estados')
    estado_anterior = models.CharField(max_length=20)
    estado_nuevo = models.CharField(max_length=20)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    justificacion = models.TextField(blank=True)

class Historial(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    entidad = models.CharField(max_length=100)
    accion = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField(auto_now_add=True)