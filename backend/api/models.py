from django.db import models

class TipoDespacho(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20, null=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

class EstadoPedido(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20, null=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True) 
    actived = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class Marca(models.Model): 
    id = models.AutoField( primary_key=True)
    nombre = models.CharField(max_length=50)
    actived = models.IntegerField(blank=True, null=True)  
    edited = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    precio = models.IntegerField(null=False,default=0)
    categorias = models.ManyToManyField(Categoria)  
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    actived = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre





class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True) 
    actived = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Persona(models.Model):
    rut    = models.IntegerField( primary_key=True)
    dv    = models.CharField(max_length=1)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    appaterno = models.CharField(max_length=30, blank=True, null=True)
    apmaterno = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=False)
    telefono = models.CharField(max_length=15)
    fechaNacimiento = models.DateField(auto_now_add=True, blank=True, null=True)
    genero = models.ForeignKey(Genero, models.DO_NOTHING)
    actived = models.IntegerField(blank=True, null=True)  
    edited = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

class Cargo(models.Model): 
    id = models.AutoField(null=False, primary_key=True)
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    actived = models.IntegerField(blank=True, null=True)  
    edited = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.ForeignKey(Persona, models.DO_NOTHING,default=1)
    nombre = models.CharField(max_length=100)
    codCargo = models.ForeignKey(Cargo, models.DO_NOTHING,default=1)
    sueldo = models.IntegerField(null=False,default=0)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    actived = models.IntegerField(blank=True, null=True)  

def cargarFoto(instance, filename):
    return "fotos/foto_{0}_{1}".format(instance.rut, filename )

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.ForeignKey(Persona, models.DO_NOTHING)
    usuario=models.CharField(unique=True,max_length=20, null=False)
    clave=models.CharField(max_length=10, null=False)
    
    def __str__(self):
        return self.usuario

class Cliente(models.Model): 
    rut    = models.OneToOneField(Persona, models.DO_NOTHING, primary_key=True)
    #foto  = models.ImageField(upload_to=cargarFoto, null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    actived = models.IntegerField(blank=True, null=True) 

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING)
    actived = models.IntegerField(blank=True, null=True)
    edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

class Tarjeta(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100,null=True)
    numero = models.IntegerField()
    csv = models.IntegerField()  
    mesvenc = models.IntegerField(null=True)
    annovenc = models.IntegerField(null=True)
    actived = models.IntegerField(blank=True, null=True)
    edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

class FormaPago(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    actived = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, null=True)
    numeracion = models.IntegerField( null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    
class personaFactura(models.Model):
    id =  models.IntegerField( primary_key=True)
    rut    = models.IntegerField()
    dv    = models.CharField(max_length=1)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    numero = models.IntegerField()
    ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING)


class RetiroPersona(models.Model):

    rut    = models.IntegerField( primary_key=True)
    dv    = models.CharField(max_length=1)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100,null=True)


class Factura(models.Model):

    personaFactura = models.ForeignKey(personaFactura, on_delete=models.CASCADE, null=True)
    numero = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True)  
    retiroPersona = models.ForeignKey(RetiroPersona, on_delete=models.CASCADE, null=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True)
    tipoDespacho = models.ForeignKey(TipoDespacho, on_delete=models.CASCADE, null=True)
    estadoPedido = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE, null=True)
    fecha_emision = models.DateField(auto_now_add=True)
    forma_pago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    precio_total = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)


class Boleta(models.Model):

    numero = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True)  
    retiroPersona = models.ForeignKey(RetiroPersona, on_delete=models.CASCADE, null=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True)
    tipoDespacho = models.ForeignKey(TipoDespacho, on_delete=models.CASCADE, null=True)
    estadoPedido = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE, null=True)
    fecha_emision = models.DateField(auto_now_add=True)
    forma_pago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    precio_total = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

class DetalleFactura(models.Model):

    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.IntegerField()
    subtotal = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

class DetalleBoleta(models.Model):

    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.IntegerField()
    subtotal = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)



class Atributo(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)



class ValorAtributo(models.Model):

    id = models.AutoField(primary_key=True)
    valor = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

class TipoProductoAtributo(models.Model):

    id = models.AutoField(primary_key=True)
    atributo = models.ForeignKey(Atributo, on_delete=models.CASCADE)
    valorAtributo = models.ForeignKey(ValorAtributo, on_delete=models.CASCADE,null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)




class ViewCliente(models.Model):

    rut = models.IntegerField( primary_key=True)
    dv=models.CharField(max_length=1, null=False)
    nombre=models.CharField(max_length=20, null=False)
    appaterno=models.CharField(max_length=20, null=False)
    apmaterno=models.CharField(max_length=20, null=False)
    email=models.CharField(max_length=20, null=False)
    genero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='genero')
    ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad')
    usuario=models.CharField(max_length=20, null=False)

    class Meta:
    	db_table = 'view_cliente'

class Bodega(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)  
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre


class ProductoCantidad(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    cantidad = models.IntegerField( )
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)






class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad = models.IntegerField( )
    documento= models.CharField(max_length=100, null=True)
    envio= models.CharField(max_length=100, null=True)

    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True)  
    retiroPersona = models.ForeignKey(RetiroPersona, on_delete=models.CASCADE, null=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True)
    tipoDespacho = models.ForeignKey(TipoDespacho, on_delete=models.CASCADE, null=True)

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)




class MovimientoBodega(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_ida = models.DateTimeField()
    fecha_llegada = models.DateTimeField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  
    bodega_origen = models.ForeignKey(Bodega, related_name='movimientos_origen', on_delete=models.CASCADE)  
    bodega_destino = models.ForeignKey(Bodega, related_name='movimientos_destino', on_delete=models.CASCADE) 
    cantidad = models.PositiveIntegerField()
    observaciones = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID: {self.id}, Producto: {self.producto}, Cantidad: {self.cantidad}"
    