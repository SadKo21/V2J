from django.shortcuts import render , redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer
# Create your views here.


class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


def home(request):

    productos = Producto.objects.all()
    data = {"productos": productos}
    return render(request, 'tienda/index.html', data)

@permission_required('tienda.agregar_producto')
def agregar_producto(request):
    data = {'form': ProductoForm()}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "GUARDADO CORRECTAMENTE"
        else:
            data['form'] = formulario

    return render(request, 'tienda/producto/agregar.html', data)
@permission_required('tienda.listar_producto')
def listar_producto(request):
    productos = Producto.objects.all()
    data = {"productos": productos}
    return render(request, 'tienda/producto/listar.html', data)
@permission_required('tienda.modificar_producto')
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {'form' : ProductoForm(instance=producto)}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto Modificado Correctamente"
            return redirect(to="listar-producto")
            data['form'] = formulario
    return render(request, 'tienda/producto/modificar.html', data)
@permission_required('tienda.eliminar_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar-producto")


def registro(request):
    data = {
        'form': CustomUserCreationForm
        }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            #redirigir al home
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)