from django.urls import path
from administrador.views import categoria,eliminarCategoria, eliminarProducto, producto
urlpatterns = [
    path('categoria/',categoria , name='admin_categoria'),
    path('Eliminar/<int:id>',eliminarCategoria , name='eliminar_categoria'),
    path("producto", producto, name="admin_producto"),
    path('Eliminar/<int:id>',eliminarProducto , name='eliminar_Producto'),
]