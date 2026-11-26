from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

#Una de las cosas que agrege en los models fue el "on_delete=models."protect" <- este protect es mas que nada que si un dato esta relacionado con otro no lo puede eliminar, teniendo mayor gestion y control con el tema de cancelaciones u otras cosas. tip pro sioke xd

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]) ## que el minimo valor sea 0
    activo = models.BooleanField(default=True)
    
    def __str__(self): 
        return self.nombre

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

    def __str__(self):
        return f"Pedido {self.pk} - {self.usuario} - {self.fecha_servicio}"


class DetallePedido(models.Model): # tabla intermedia entre pedido y producto, se hizo de esta forma porque se necesita un dato propio (cantidad) por eso no se utilizo manytomany
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, related_name='detalles')
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=['pedido', 'producto'],name='producto_unico_por_pedido')]

    def __str__(self):
        return f"{self.cantidad} x {self.producto}"

class EstadoPreparacion(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, related_name='historial_estados')
    estado_anterior = models.CharField(max_length=20, choices=Pedido.ESTADOS_PREPARACION)
    estado_nuevo = models.CharField(max_length=20, choices=Pedido.ESTADOS_PREPARACION)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    justificacion = models.TextField(blank=True)

    def __str__(self):
        return f"Pedido {self.pedido_id}: {self.estado_anterior} -> {self.estado_nuevo}"


class Historial(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, null= True, blank=True) # el null true acepta que la base de datos acepta que esa columna quede vacia, 
    entidad = models.CharField(max_length=100)                                           #y blank true el admin y los formularios de django aceptan dejar el campo vacio
    accion = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.accion}"