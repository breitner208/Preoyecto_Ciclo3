from django.shortcuts import render

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
        empresa = Empresa(id=data['id'],nit=data['nit'],nombre=data['nombre'],ciudad=data['ciudad'],direccion=data['direccion'],telefono=data['telefono'],sector_productivo=data['sector_productivo'],fecha=data['fecha'])
        empresa.save()
        datos={'mensaje':'Empresa registrada exitosamente'}
        return JsonResponse(datos)

    def put(self,request,id):
        data=json.loads(request.body)
        empresa=list(Empresa.objects.filter(id=id).values())
        if len(empresa)>0:
            empr=Empresa.objects.get(id=id)
            empr.nit=data["nit"]
            empr.nombre=data["nombre"]
            empr.ciudad=data["ciudad"]
            empr.direccion=data["direccion"]
            empr.telefono=data["telefono"]
            empr.sector_productivo=data["sector_productivo"]
            empr.fecha=data["fecha"]
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

class EmpleadosView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get (self,request,documento=""):

        if len(documento)>0:
            empleado=list(Empleados.objects.filter(documento=documento).values())
            if len(empleado)>0:
                datos={"Empleados":empleado}
            else:
                datos={"mensaje":"No se encontro el usuario."}
        else:
            empleado=list(Empleados.objects.values())
            if len(empleado)>0:
                datos={"mensaje":empleado}
            else:
                datos={"mensaje":"No se encontraron el usuario."}
       
        return JsonResponse(datos)

    def post(self,request):
        data=json.loads(request.body) 
        empresa1=Empresa.objects.get(id=data["id"])
        empresa=Empleados.objects.create(empresa1)
        empresa = Empleados(documento=data['documento'],nombre=data['nombre'],apellidos=data['apellidos'],email=data['email'],telefono=data['telefono'],id=data['id'],fecha=data['fecha'])
        empresa.save()
        datos={'mensaje':'Empleado registrado exitosamente'}
        return JsonResponse(datos)
