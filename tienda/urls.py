from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('agregar-producto', views.agregar_producto, name='agregar-producto'),
    path('listar-producto', views.listar_producto, name='listar-producto'),
    path('modificar-producto/<id>', views.modificar_producto, name='modificar-producto'),
    path('eliminar-producto/<id>', views.eliminar_producto, name='eliminar-producto'),
]
