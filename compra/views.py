from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
# Create your views here.
def lista_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, "lista_proveedores.html",{"proveedores":proveedores})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "lista_productos.html",{"productos":productos})

def index(request):
    return render(request, "index.html")

class CrearProveedor(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name= "crear_proveedor.html"
    success_url = reverse_lazy('lista_proveedores')

class CrearProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "crear_producto.html"
    success_url = reverse_lazy("lista_productos")

def json_proveedor(request):
    proveedores = Proveedor.objects.all().values()
    return JsonResponse(list(proveedores),safe=False)

@csrf_exempt
def postProveedor(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        nombre = data.get("nombre")
        apellido = data.get("apellido")
        dni = data.get("dni")

        nuevo_proveedor = Proveedor(nombre =nombre, apellido = apellido, dni=dni)
        nuevo_proveedor.save()

        return JsonResponse({"mensaje":"Creado exitosamente"})