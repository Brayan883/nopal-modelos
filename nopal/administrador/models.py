from django.db import models
from django.utils.translation import gettext_lazy as _

class Categoria(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombre', help_text='Ingrese Nombre')
    descripcion = models.TextField(max_length=20,verbose_name='Descripción')
    foto = models.ImageField(upload_to='imagenes/', null=True, blank=True , verbose_name='Foto' )
    def __str__(self):
        texto = ' {0} {1}'
        return texto.format(self.nombre,self.descripcion)

class Marca(models.Model):
    nombre = models.CharField(max_length=45, verbose_name='Nombre', help_text='Ingrese Nombre')
    def __str__(self):
        return '%s'%self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=45, verbose_name='Nombre', help_text='Ingrese Nombre')  
    precio = models.FloatField(verbose_name='Precio')  
    fechaVencimiento = models.DateField(verbose_name='Fecha Vencimiento')
    porcentajeGanancia = models.FloatField(verbose_name='Porcentaje Ganancia')
    unidadMedida = models.CharField(max_length=10, verbose_name='Unidad de Medida')
    stock = models.SmallIntegerField(verbose_name='Stock')
    foto = models.ImageField(upload_to='imagenes/', null=True, blank=True , verbose_name='Foto' )
    categoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL, null=True,verbose_name=u"Categoria")
    marca = models.ForeignKey(Marca,on_delete=models.SET_NULL, null=True,verbose_name=u"Marca")
    def __str__(self):
        texto = '{0} {1} {2} '
        return texto.format(self.nombre,self.precio, self.fechaVencimiento)
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=45, verbose_name='Nombre', help_text='Ingrese Nombre')
    telefono = models.CharField(max_length=13, verbose_name='Telefono')
    correo = models.EmailField(max_length=45, verbose_name='Correo', blank=True )
    def __str__(self):
        return '%s %s %s'%self.nombre,self.telefono,self.correo
    
class Compra(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    precio_total = models.FloatField(verbose_name='Precio Total')
    proveedor=models.ForeignKey(Proveedor,on_delete=models.SET_NULL, null=True,verbose_name=u"Proveedor")
    def __str__(self):
        return '%s'%self.fecha
    
class DetalleCompra(models.Model):
    cantidad = models.IntegerField(verbose_name='Cantidad')
    iva = models.FloatField(verbose_name='Iva')
    valor_parcial = models.FloatField(verbose_name='Valor Parcial')
    class Pago(models.TextChoices):
        Datafono = 'Datafono', _('Datafono')
        Efectivo = 'Efectivo', _('Efectivo')
        Transaccion = 'Transacción', _('Transacción')
    Metodo_pago = models.CharField(max_length=20,choices=Pago.choices, verbose_name='Metodo Pago')
    compra = models.ForeignKey(Compra,on_delete=models.SET_NULL, null=True,verbose_name=u"Compra")
    producto = models.ForeignKey(Producto,on_delete=models.SET_NULL, null=True,verbose_name=u"Producto")
    def __str__(self):
        return '%s'%self.cantidad
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=45, verbose_name='Nombre', help_text='Ingrese Nombre')
    apellido = models.CharField(max_length=45, verbose_name='Apellido', help_text='Ingrese Apellido' )
    class Documento(models.TextChoices):
        Cedula_C = 'Cédula de Ciudadanía' , _('Cédula de Ciudadanía')
        Cedula_E = 'Cédula de Extranjeria',_('Cédula de Extranjeria')
        
    tipo_documento = models.CharField(max_length=21,choices=Documento.choices ,verbose_name='Tipo Documento')
    Numero_Documento = models.IntegerField( verbose_name='Numero Documento')
    telefono = models.CharField(max_length=13 , verbose_name='Telefono')
    direccion = models.CharField(max_length=45, verbose_name='Dirección')
    fechaNacimiento=models.DateField(verbose_name='Fecha Nacimiento')
    class Rol(models.TextChoices):
        Administrador = 'Administrador' , _('Administrador')
        Vendedor = 'Vendedor',_('Vendedor')  
        
    rol = models.CharField(max_length=20,choices=Rol.choices ,verbose_name='Rol')  
    usuario =  models.CharField(max_length=20, verbose_name='Usuario' , blank=True )
    contraseña = models.CharField(max_length=45 , verbose_name='Contraseña' , blank=True )
    class Estado(models.TextChoices):
        Activo = 'Activo',_('Activo')
        Inactivo = 'Inactivo',_('Inactivo')
    estado = models.CharField(max_length=20,choices=Estado.choices, verbose_name='Estado')
    
    def __str__(self):
        return '%s %s'%self.nombre,self.apellido

    
class Domicilio(models.Model):
    fecha = models.DateTimeField(verbose_name='Fecha')
    class Estado(models.TextChoices):
        Activo = 'Entregad',_('Entregado')
        Inactivo = 'Cancelado',_('Cancelado')
    estado = models.CharField(max_length=20,choices=Estado.choices, verbose_name='Estado')
    observaciones = models.CharField(max_length=45, verbose_name='Observaciones' , blank=True )
    empleado = models.ForeignKey(Empleado,on_delete=models.SET_NULL, null=True,verbose_name=u"Empleado")
    def __str__(self):
        return '%s'%self.fecha
    

    
class Venta(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    Precio_Total = models.FloatField(verbose_name='Precio Total')
    class Venta_Opcion(models.TextChoices):
        local = 'local', _('Local')
        Domicilio = 'Domicilio', _('Domicilio')
    Tipo_Venta = models.CharField(max_length=20,choices=Venta_Opcion.choices, verbose_name='Tipo Venta')
    Iva = models.FloatField(verbose_name='Iva')
    empleado = models.ForeignKey(Empleado,on_delete=models.SET_NULL, null=True,verbose_name=u"Empleado")
    domicilio = models.ForeignKey(Domicilio,on_delete=models.SET_NULL, null=True,verbose_name=u"Domicilio")
    def __str__(self):
        return '%s %s'%self.fecha,self.Precio_Total
        
class DetalleVenta(models.Model):
    cantidad = models.IntegerField(verbose_name='Cantidad')
    iva = models.FloatField(verbose_name='Iva')
    valor_parcial = models.FloatField(verbose_name='Valor Parcial')
    class Pago(models.TextChoices):
        Datafono = 'Datafono', _('Datafono')
        Efectivo = 'Efectivo', _('Efectivo')
        Transaccion = 'Transacción', _('Transacción')
    Metodo_pago = models.CharField(max_length=20,choices=Pago.choices, verbose_name='Metodo Pago')
    venta = models.ForeignKey(Venta,on_delete=models.SET_NULL, null=True,verbose_name=u"Venta")
    producto = models.ForeignKey(Producto,on_delete=models.SET_NULL, null=True,verbose_name=u"Producto")
    def __str__(self):
        return '%s'%self.cantidad



class Cliente(models.Model):
    nombre = models.CharField(max_length=45, verbose_name='Nombre', help_text='Ingrese Nombre')
    apellido = models.CharField(max_length=45, verbose_name='Apellido', help_text='Ingrese Apellido' )
    class Documento(models.TextChoices):
        Cedula_C = 'Cédula de Ciudadanía' , _('Cédula de Ciudadanía')
        Cedula_E = 'Cédula de Extranjeria',_('Cédula de Extranjeria')
        
    tipo_documento = models.CharField(max_length=21,choices=Documento.choices ,verbose_name='Tipo Documento')
    Numero_Documento = models.IntegerField(verbose_name='Numero Documento')
    telefono = models.CharField(max_length=13 , verbose_name='Telefono')
    usuario = models.CharField(max_length=20, blank=True , verbose_name='Usuario')
    contraseña = models.CharField(max_length=45 , verbose_name='Contraseña')
    class Estado(models.TextChoices):
        Activo = 'Activo',_('Activo')
        Inactivo = 'Inactivo',_('Inactivo')
    estado = models.CharField(max_length=20,choices=Estado.choices, verbose_name='Estado')
    def __str__(self):
        return '%s %s'%self.nombre,self.apellido
    
    
class Direccion(models.Model):
    descripcion = models.CharField(max_length=20 , verbose_name='Descripción')
    barrio = models.CharField(max_length=20, verbose_name='Barrio')
    municipio = models.CharField(max_length=15,verbose_name='Municipio', blank=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.SET_NULL, null=True,verbose_name=u"Cliente")
    def __str__(self):
        return '%s'%self.descripcion