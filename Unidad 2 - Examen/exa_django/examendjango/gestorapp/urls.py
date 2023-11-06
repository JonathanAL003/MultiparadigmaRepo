from django.urls import path
from . import views

app_name = 'gestorapp' 

urlpatterns = [
    path('', views.index, name='index'),  
    path('clientes/', views.clientes_list, name='clientes_list'), 
    path('clientes/<int:cliente_id>/', views.cliente_detalle, name='cliente_detalle'), 
    path('clientes/nuevo/', views.cliente_nuevo, name='cliente_nuevo'),  
    path('clientes/editar/<int:cliente_id>/', views.cliente_editar, name='cliente_editar'), 
    path('clientes/eliminar/<int:cliente_id>/', views.cliente_eliminar, name='cliente_eliminar'),
]
