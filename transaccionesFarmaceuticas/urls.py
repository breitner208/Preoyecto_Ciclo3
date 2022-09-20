from django.urls import path

from transaccionesFarmaceuticas.views import EmpresaView
from transaccionesFarmaceuticas.views import UsuarioView
from transaccionesFarmaceuticas.views import EmpleadosView

urlpatterns = [
    path('empresa/', EmpresaView.as_view(), name='listar'),    
    path('empresa/<str:id>', EmpresaView.as_view(), name='Buscar'),
    path('usuarios/', UsuarioView.as_view(), name='ver usuario'),
    path('empleados/<str:id>', EmpleadosView.as_view(), name='Buscar'),
    path('empleados/', EmpleadosView.as_view(), name='ver empleado')
    
]
