from django.shortcuts import render , redirect
from administrador.forms import FormCategoria, FormProducto
from django.contrib import  messages
from administrador.models import Categoria, Producto
# Create your views here.
def categoria(request):
    titulo = 'Gestionar Categoria'
    categoria_db = Categoria.objects.all()
    if request.method == 'POST':
        form = FormCategoria(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Dato Guardado Correctamente')
            return redirect('admin_categoria')
        else:
            messages.warning(request, 'El Dato No Se Guardo')
            return redirect('admin_categoria')
    else:
        form = FormCategoria()
        context = {
            'categorias':categoria_db,
            'form':form,
            'titulo':titulo
        }
        return render(request, 'admin_categoria.html' , context )
    
def eliminarCategoria(request,id):
    categoria_db = Categoria.objects.get(id = id)
    categoria_db.delete()
    messages.success(request,'Dato Eliminado Correctamente')
    return redirect('admin_categoria')
   
        
# def editarCategoria(request,id):
#     categoria_db = Categoria.objects.get(id = id)
#     if request.method == 'POST':
#         form = FormCategoria(request.POST, instance= categoria_db)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Dato Editado Correctamente')
#             return redirect('admin_categoria')
#         else:
#             messages.warning(request,'El Dato No Se Edito')
#             return redirect('admin_categoria')
#     else:
#         form = FormCategoria()
#         context = {
#             'form':form
#         }
#         return render(request,'',context)

def producto(request):
    titulo = 'Gestionar Producto'
    producto_db = Producto.objects.all()
    if request.method == 'POST':
        form = FormProducto(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Dato Guardado Correctamente')
            return redirect('admin_producto')
        else:
            messages.warning(request, 'El Dato No Se Guardo')
            return redirect('admin_producto')
    else:
        form = FormProducto()
        context = {
            'categorias':producto_db,
            'form':form,
            'titulo':titulo
        }
        return render(request, 'admin_producto.html' , context )
    
def eliminarProducto(request , id ):
    producto_db = Producto.objects.get(id = id)
    producto_db.delete()
    messages.success(request,'Dato Eliminado Correctamente')
    return redirect('admin_producto')