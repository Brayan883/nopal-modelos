from django import forms
from administrador.models import *
class FormCategoria(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control form-control-sm',
        'rows':3,
        'cols':150,
    }))
    class Meta:
        model = Categoria
        fields ='__all__'

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','precio','fechaVencimiento','porcentajeGanancia','unidadMedida','stock','foto']
class FormMarca(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
class FormDetalleCompra(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = '__all__'
class FormDetalleVenta(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = '__all__'
        
class  FormProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
class FormCompra(forms.ModelForm):
     class Meta:
        model = Compra
        fields = '__all__'
class FormVenta(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        
class FormDireccion(forms.ModelForm):
     class Meta:
        model = Direccion
        fields = '__all__'
class FormCliente(forms.ModelForm):
     class Meta:
        model = Cliente
        fields = '__all__'
class FormCliente(forms.ModelForm):
     class Meta:
        model = Domicilio
        fields = '__all__'
class FormEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
    