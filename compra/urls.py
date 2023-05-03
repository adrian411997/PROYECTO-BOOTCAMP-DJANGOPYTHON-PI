from .views import *
from django.urls import path

urlpatterns = [
    path("proveedores/", lista_proveedor, name="lista_proveedores"),
    path("proveedores/crear", CrearProveedor.as_view(),name="crear_proveedor"),
    path("producto", lista_productos, name="lista_productos"),
    path("productos/crear", CrearProducto.as_view(),name="crear_productos"),
    path("",index,name="index"),
    path("api/proveedores", json_proveedor),
    path("api/proveedores/crear", postProveedor)

]
