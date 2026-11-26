from django.shortcuts import render
from django.utils import timezone
from .decorators import rol_requerido
from .services import verificar_rol, obtener_consolidado
from .models import Pedido
from datetime import date
from django.contrib import messages
from django.shortcuts import redirect
from .services import cambiar_estado_pedido
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import LoginView
from .models import Historial

# Create your views here.

##QUE HACE LISTA DE PEDIDOS:

#Fecha: permite consultar los pedidos de una fecha; si no se especifica, utiliza la fecha actual.
#Pedidos: obtiene los pedidos confirmados desde la base de datos.
#Trabajador: obtiene el usuario asociado al pedido.
#Detalles: carga los productos y sus cantidades.
#Filtro: permite filtrar por pendiente, en_preparacion o preparado.
#Acceso: exige pertenecer al grupo Cocina.


@rol_requerido("Cocina")
def lista_pedidos(request):
    fecha = request.GET.get("fecha", "")

    try:
        fecha = date.fromisoformat(fecha)
    except (ValueError, TypeError):
        fecha = timezone.localdate()

    estado = request.GET.get("estado", "")

    pedidos = Pedido.objects.filter(
        fecha_servicio=fecha,
        estado="confirmado"
    ).select_related("usuario").prefetch_related(
        "detalles__producto"
    ).order_by("fecha_hora_creacion")

    if estado:
        pedidos = pedidos.filter(estado_preparacion=estado)

    return render(request, "Cocinaapp/pedidos.html", {
        "pedidos": pedidos,
        "fecha": fecha,
        "estado": estado
    })


##QUE HACE CONSOLIDADO COCINA:

#Seleccionar una fecha para consultar.
#Obtener los productos consolidados desde MySQL.
#Excluir pedidos cancelados, gracias al servicio que ya construimos.
#Restringir el acceso al grupo Cocina.
#Mostrar los datos a través de una plantilla HTML.


@rol_requerido("Cocina")
def consolidado_cocina(request):
    fecha = request.GET.get("fecha", "")

    try:
        fecha = timezone.datetime.strptime(fecha, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        fecha = timezone.localdate()

    productos = obtener_consolidado(fecha)

    return render(request, "Cocinaapp/consolidado.html", {
        "productos": productos,
        "fecha": fecha
    })

@rol_requerido("Cocina")
def actualizar_pedido(request, pedido_id):
    if request.method != "POST":
        return redirect("lista_pedidos")

    nuevo_estado = request.POST.get("estado")
    justificacion = request.POST.get("justificacion", "")

    try:
        cambiar_estado_pedido(
            pedido_id=pedido_id,
            nuevo_estado=nuevo_estado,
            usuario=request.user,
            justificacion=justificacion
        )

        messages.success(request, "El estado del pedido se actualizó correctamente.")

    except (ValueError, PermissionDenied) as error:
        messages.error(request, str(error))

    except Pedido.DoesNotExist:
        messages.error(request, "El pedido solicitado no existe.")

    return redirect("lista_pedidos")

class LoginRegistrado(LoginView):
    template_name = "Cocinaapp/login.html"

    def form_valid(self, form):

        respuesta = super().form_valid(form)
        Historial.objects.create(
            usuario = self.request.user,
            entidad = 'Sesion',
            accion = 'Inicio de sesion'
        )

        return respuesta 

