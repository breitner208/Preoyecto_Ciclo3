from django.db import models

# Create your models here.
class Empresa(models.Model):
    id=models.AutoField(primary_key=True)
    nit=models.IntegerField(unique=True,null=False)
    nombre=models.TextField(max_length=100,unique=True,null=False)
    ciudad=models.CharField(max_length=50,null=False)
    direccion=models.IntegerField(null=False)
    telefono=models.CharField(max_length=50)
    sector_productivo=models.CharField(max_length=50,null=False)
    fecha=models.DateField(auto_now=True) 

class Empleados(models.Model):
    documento=models.IntegerField(primary_key=True)
    nombre=models.TextField(max_length=50,null=False)
    apellidos=models.TextField(max_length=50,null=False)
    email=models.EmailField(unique=True)
    telefono=models.CharField(max_length=50)
    id=models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha=models.DateField(auto_now=True)

class Rol(models.Model):
    empleado=models.TextField(unique=True)
    administrador=models.TextField(unique=True)
    

class Usuarios(models.Model):
    id=models.AutoField(primary_key=True)
    nombre_usuario=models.TextField(max_length=50,null=False)
    email=models.OneToOneField(Empleados, on_delete=models.CASCADE)
    password=models.TextField(max_length=50,null=False)
    rol=models.ForeignKey(Rol, on_delete=models.CASCADE)
    fecha=models.DateField(auto_now=True)


class Transaccion(models.Model):
    id=models.AutoField(primary_key=True)
    fecha=models.DateField(auto_now=True)
    concepto=models.TextField(unique=True)
    monto=models.CharField(max_length=50)
    usuario=models.ForeignKey(Rol, on_delete=models.CASCADE)
    tipo=models.TextField(unique=True)
    fecha=models.DateField(auto_now=True)


    
