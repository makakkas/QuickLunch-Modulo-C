from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

## EXPLICACION DE QUE HICE ACA !!
##login_required: exige que el usuario haya iniciado sesión.
##groups.filter(name=rol).exists(): verifica si pertenece al grupo requerido.
##HttpResponseForbidden: responde con HTTP 403 si no tiene el rol.
##rol_requerido("Cocina"): después podremos proteger cada vista de Cocina con una sola línea.

####################################################

def rol_requerido(rol):
    def decorador(view_func):
        @login_required
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name=rol).exists():
                return view_func(request, *args, **kwargs)

            return HttpResponseForbidden("Acceso denegado")

        return wrapper
    return decorador