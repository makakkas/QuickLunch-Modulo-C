from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_pedidos, name="lista_pedidos"),
    path("consolidado/", views.consolidado_cocina, name="consolidado_cocina"),
    path("pedido/<int:pedido_id>/actualizar/", views.actualizar_pedido, name="actualizar_pedido"),
]