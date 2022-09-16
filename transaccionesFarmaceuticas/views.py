from django.shortcuts import render

# Create your views here.
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from transaccionesFarmaceuticas.models import Empresa
from django.http import JsonResponse

import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from transaccionesFarmaceuticas.models import Empresa,Empleados,Usuarios
from django.http import JsonResponse

# Create your views here.

class EmpresaView(View): 

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get (self,request,id=""):

        if len(id)>0:
            empresas=list(Empresa.objects.filter(id=id).values())
            if len(empresas)>0:
                datos={"Empresa":empresas}
            else:
                datos={"mensaje":"No se encontro la Empresa."}
        else:
            empresas=list(Empresa.objects.values())
            if len(empresas)>0:
                datos={"mensaje":empresas}
            else:
                datos={"mensaje":"No se encontraron empresas."}
       
        return JsonResponse(datos)


    def post(self,request):
        data=json.loads(request.body)
        Empresa = Empresa(id=data['id'],nit=data['nit'],nombre=data['nombre'],ciudad=data['ciudad'],direccion=data['direccion'],telefono=data['telefono'],sector=data['sector'],fecha=data['fecha'])
        Empresa.save()
        datos={'mensaje':'Empresa registrada exitosamente'}
        return JsonResponse(datos)

    def put(self,request,id):
        data=json.loads(request.body)
        Empresa=list(Empresa.objects.filter(id=id).values())
        if len(Empresa)>0:
            empr=Empresa.objects.get(id=id)
            empr.nit=data["nit"]
            empr.nombre=data["nombre"]
            empr.ciudad=data["ciudad"]
            empr.direccion=data["direccion"]
            empr.telefono=data["telefono"]
            empr.sector=data["sector"]
            empr.no_page=data["fecha"]
            empr.save()
            mensaje={"mensaje":"Empresa actualizada exitosamente."}
        else:
            mensaje={"mensaje":"No se encontro la empresa."}
        return JsonResponse(mensaje)

    def delete(self,request,isbn):
        empresa=list(Empresa.objects.filter(id=id).values())
        if len(empresa)>0:
            emp=Empresa.objects.filter(id=id).delete()
            mensaje={"mensaje":"Empresa eliminada exitosamente."}
        else:
            mensaje={"mensaje":"No se encontro la Empresa."}
        return JsonResponse(mensaje)

class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request):
        data=json.loads(request.body)
        try:
            usu=Usuarios.objects.get(id=data["id"])
            cont=Usuarios.objects.get(password=data["password"])
            usu=Usuarios.objects.create(id=id,cont=cont)
            usu.save()
            mensaje={"mensaje":"Usuario Registrado."}
        except usu.DoesNotExist:
            mensaje={"mensaje":"El Usuario no existe."}
        except cont.DoesNotExist:
            mensaje={"mensaje":"La contrasena no existe."}

        return JsonResponse(mensaje)

class EmpleadoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post (self, request):
        data=json.loads(request.body)
        try:
            empl=Empleados.objects.get(documento=data["documento"])
            empl=Empleados.objects.create(empleado=empl)
            empl.save()
            mensaje={"mensaje":"Empleado Registrado."}
        except Empleados.DoesNotExist:
            mensaje={"mensaje":"Empleado no existe."}
        except Empleados.DoesNotExist:
            mensaje={"mensaje":"empleado ya existe ."}

        return JsonResponse(mensaje)