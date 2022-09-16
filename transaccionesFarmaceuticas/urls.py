from django.urls import path

from transaccionesFarmaceuticas.views import EmpresaView
from transaccionesFarmaceuticas.views import UsuarioView
from transaccionesFarmaceuticas.views import EmpleadoView

urlpatterns = [
    path('empresa/', EmpresaView.as_view(), name='listar'),    
    path('empresa/<str:id>', EmpresaView.as_view(), name='Buscar'),
    path('usuarios/', UsuarioView.as_view(), name='ver usuario'),
    path('Empleados/', EmpleadoView.as_view(), name='ver empleado')
    
]
