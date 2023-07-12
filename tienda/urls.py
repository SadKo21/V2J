from django.urls import path, include
from . import views
from .views import home , registro, ProductoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)

urlpatterns = [
    path('', home, name='home'),
    path('', views.home, name='index'),
    path('agregar-producto', views.agregar_producto, name='agregar-producto'),
    path('listar-producto', views.listar_producto, name='listar-producto'),
    path('modificar-producto/<id>', views.modificar_producto, name='modificar-producto'),
    path('eliminar-producto/<id>', views.eliminar_producto, name='eliminar-producto'),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
]
