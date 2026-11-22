from django.db import transaction
from django.db.models import Sum
from django.core.exceptions import PermissionDenied
from .models import Pedido, DetallePedido, EstadoPreparacion, Historial

###EXPLCACION DE QUE HICE ACA LOL

#Busca los detalles de pedidos para una fecha específica.
#Solo considera pedidos confirmados.
#Agrupa los productos iguales.
#Suma sus cantidades.
#Ordena el resultado por nombre del producto.

# Seguridad: comprueba que el usuario pertenece a Cocina.
# Bloqueo: select_for_update() evita conflictos al modificar simultáneamente un pedido.
# Validación: no permite saltarse etapas ni repetir el estado.
# Retroceso: exige una justificación.
# Historial: registra quién cambió el estado, el estado anterior, el nuevo y la fecha.
# Atomicidad: transaction.atomic evita que se guarde parcialmente la operación si ocurre un error.
# Ojo: si el retroceso se intenta sin justificación, se lanza un error y no se guarda el cambio.

###ALGO IMPORTANTE QUE RECALCAR DE ESTO

## utilizamos "confirmado" suponiendo que ese es el valor real que definiste en tu modelo Pedido. Si lo dejaste como "confirmed", tendremos que usar ese valor exacto, HAY QUE TENER CUIDADO CON ESTO LOL.

###########################



def verificar_rol(usuario, rol):
    if not usuario.groups.filter(name=rol).exists():
        raise PermissionDenied("No tienes permisos para realizar esta acción.")

def obtener_consolidado(fecha):
    detalles = DetallePedido.objects.filter(
        pedido__fecha_servicio=fecha,
        pedido__estado="confirmado"
    ).values(
        "producto__nombre"
    ).annotate(
        total=Sum("cantidad")
    ).order_by("producto__nombre")

    return detalles

@transaction.atomic
def cambiar_estado_pedido(pedido_id, nuevo_estado, usuario, justificacion=""):
    verificar_rol(usuario, "Cocina")

    pedido = Pedido.objects.select_for_update().get(id=pedido_id)

    if pedido.estado != "confirmado":
        raise ValueError("No se puede modificar un pedido cancelado.")

    estados = ["pendiente", "en_preparacion", "preparado"]

    estado_actual = pedido.estado_preparacion

    if nuevo_estado not in estados:
        raise ValueError("El estado solicitado no es válido.")

    if nuevo_estado == estado_actual:
        raise ValueError("El pedido ya se encuentra en ese estado.")

    posicion_actual = estados.index(estado_actual)
    posicion_nueva = estados.index(nuevo_estado)

    if posicion_nueva > posicion_actual + 1:
        raise ValueError("No se permite saltar estados.")

    if posicion_nueva < posicion_actual:
        if not justificacion.strip():
            raise ValueError("Debe justificar el retroceso.")

    EstadoPreparacion.objects.create(
        pedido=pedido,
        estado_anterior=estado_actual,
        estado_nuevo=nuevo_estado,
        usuario=usuario,
        justificacion=justificacion
    )

    pedido.estado_preparacion = nuevo_estado
    pedido.save(update_fields=["estado_preparacion"])

    Historial.objects.create(
        usuario=usuario,
        entidad=f"Pedido {pedido.id}",
        accion=f"Estado cambiado de {estado_actual} a {nuevo_estado}"
    )

    return pedido