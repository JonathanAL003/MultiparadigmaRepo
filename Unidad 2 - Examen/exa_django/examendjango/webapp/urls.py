from django.urls import path
from . import views

app_name = 'webapp' 
urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos_list, name='productos_list'),
    path('productos/<int:producto_id>/', views.producto_detalle, name='producto_detalle'), 
    path('productos/nuevo/', views.producto_nuevo, name='producto_nuevo'), 
    path('productos/editar/<int:producto_id>/', views.producto_editar, name='producto_editar'), 
    path('productos/eliminar/<int:producto_id>/', views.producto_eliminar, name='producto_eliminar'), 
]

