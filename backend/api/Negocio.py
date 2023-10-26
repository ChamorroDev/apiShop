from .models import *
from django.core.files.base import ContentFile
from django.conf import settings
import os
from shutil import copyfile
import base64
import shutil
class Negocio:
    def get_viewCliente( rut):
        try:
            return ViewCliente.objects.get(pk=rut)
        except ViewCliente.DoesNotExist:
            raise None
        
    def get_viewClienteAll():
        try:
            return ViewCliente.objects.all()
        except ViewCliente.DoesNotExist:
            raise None        
    def get_empleadoAll():
        try:
            return Empleado.objects.all()
        except Empleado.DoesNotExist:
            return None
    def get_cliente( rut):
        try:
            return Cliente.objects.get(pk=rut)
        except Cliente.DoesNotExist:
            return None  
    def get_empleado(rut):
        try:
            return Empleado.objects.get(rut=rut)
        except Empleado.DoesNotExist:
            return None           
    def get_persona( rut):
        try:
            return Persona.objects.get(pk=rut)
        except Persona.DoesNotExist:
            return None       
    def get_usuario( usuario):
        try:
            usuarios = Usuario.objects.filter(usuario=usuario)
            if (usuarios.count()> 0):
                return usuarios[0]
            else:
                return None
        except Usuario.DoesNotExist:
            return None
    def actualizarFotoCliente(cliente, foto):


        image_data =foto
        format, imgstr = image_data.split(';base64,')  
        ext = format.split('/')[-1]  
        image_data = base64.b64decode(imgstr)

        cliente.foto.save(f'cliente_{cliente.rut}_foto.{ext}', ContentFile(image_data), save=True)

        return cliente
    def eliminarFotoCliente(cliente):
        if cliente.foto:
            foto_path = cliente.foto.path
            os.remove(foto_path)  

            cliente.foto.delete(save=True)
        return cliente
    
    def cambiarClave(user,clave):
        usuario = Negocio.get_usuario(user)
        if (usuario!= None):
            usuario.clave=clave
            usuario.save()

        return True
    
    def usuarioCrear(rut,user,clave):
        usuario = Negocio.get_usuario(user)
        viewcliente = Negocio.get_viewCliente(rut)
        if (usuario==None):
            return False
        usuario.usuario =user
        usuario.clave =clave
        usuario.save()
        viewcliente.usuario=user
        viewcliente.save()
        return True


    def clienteCrear(rut,dv,nombres,paterno,materno,email,telefono,genero,foto):
        persona = Negocio.get_persona(int(rut))
        cliente = Negocio.get_cliente(rut)
        usuario = Negocio.get_usuario(rut)
        
        gen=Genero.objects.get(id=genero)
        ci=Ciudad.objects.get(id=1)

        if (persona== None):
            persona =  Persona(rut=rut,dv=dv,nombre=nombres,appaterno=paterno,
                               apmaterno=materno,email=email,telefono=telefono,fechaNacimiento='2023-01-01',genero=gen)
        else:
            persona.nombre=nombres
            persona.appaterno=paterno
            persona.apmaterno=materno
            persona.email=email
            persona.telefono=telefono
            persona.genero=gen

        if (cliente== None):
            
            cliente = Cliente(rut=rut)
            cliente=Negocio.actualizarFotoCliente(cliente, foto)
            
        else:
            cliente=Negocio.eliminarFotoCliente(cliente)
            
            cliente=Negocio.actualizarFotoCliente(cliente, foto)

        if (usuario== None):
            usuario = Usuario(None,rut,rut,1)
  
    
        persona.save()
        cliente.save()
        usuario.save()
        viewCliente =  ViewCliente(rut=rut,dv=dv,nombre=nombres,appaterno=paterno,
                                   apmaterno=materno,email=email,genero=gen,ciudad=ci,usuario=usuario.usuario)
        viewCliente.save()

        return True


    def clienteGet(rut):
        return Negocio.get_viewCliente(rut)
    
    def clienteEliminar(rut):
        persona = Negocio.get_persona(int(rut))
        cliente = Negocio.get_cliente(rut)
        usuario = Negocio.get_usuario(rut)
        usuario.delete()
        cliente.delete()
        persona.delete()     



    def empleadoCrear(rut,dv,nombres,paterno,materno,email,telefono,genero,cargo,sueldo):
        persona = Negocio.get_persona(int(rut))
        empleado = Negocio.get_empleado(rut)
        usuario = Negocio.get_usuario(rut)
        
        gen=Genero.objects.get(id=genero)


        if (persona== None):
            persona =  Persona(rut=rut,dv=dv,nombre=nombres,appaterno=paterno,
                               apmaterno=materno,email=email,telefono=telefono,fechaNacimiento='2023-01-01',genero=gen)
        else:
            persona.nombre=nombres
            persona.appaterno=paterno
            persona.apmaterno=materno
            persona.email=email
            persona.telefono=telefono
            persona.genero=gen

        if (empleado== None):
            
            empleado = Empleado(rut=rut,nombre=nombres,codCargo=cargo,sueldo=sueldo)
            
        else:
            empleado.nombre=nombres
            empleado.codCargo_id=cargo
            empleado.sueldo=sueldo

        if (usuario== None):
            usuario = Usuario(None,rut,rut,1)
  
    
        persona.save()
        empleado.save()
        usuario.save()
        
        return True

    def get_productoProveedorAll():
        try:
            return ProductoProveedor.objects.all()
        except ProductoProveedor.DoesNotExist:
            raise None  
    def get_proveedor(id):
        try:
            return Proveedor.objects.get(id=id)
        except Proveedor.DoesNotExist:
            raise None 
    def get_producto(id):
        try:
            return Producto.objects.get(id=id)
        except Producto.DoesNotExist:
            raise None 
    def get_productoProveedor(prov,prod):
        try:
            return ProductoProveedor.objects.get(proveedor=prov,producto=prod)
        except ProductoProveedor.DoesNotExist:
            raise None
    def get_productoProveedorAll(prod):
        try:
            return ProductoProveedor.objects.get(producto=prod)
        except ProductoProveedor.DoesNotExist:
            raise None
    def crear_ProductoProveedor(proveedor_id,producto_id,precio):
        proveedor = Negocio.get_proveedor(int(proveedor_id))
        producto = Negocio.get_producto(int(producto_id))
        provee=Negocio.get_productoProveedor(proveedor,producto)
        if (provee== None):
            provee =  Persona(proveedor=proveedor,producto=producto,cantidad=precio)
        else:
            provee.proveedor=proveedor_id
            provee.producto=producto
            provee.precio=precio

        provee.save()

        return True
    def get_bodega(id):
        try:
            return Bodega.objects.get(id=id)
        except Bodega.DoesNotExist:
            raise None
        
    def get_producto(id):
        try:
            return Producto.objects.get(id=id)
        except Producto.DoesNotExist:
            raise None
        
    def get_stockBodegaAll(bodega):
        try:
            return ProductoCantidad.objects.get(bodega=bodega)
        except ProductoCantidad.DoesNotExist:
            raise None    
    
    def get_stockBodega(producto,bodega):
        try:
            return ProductoCantidad.objects.get(producto=producto,bodega=bodega)
        except ProductoCantidad.DoesNotExist:
            raise None

    def crear_stockBodega(producto_id,bodega_id,cantidad):
        producto = Negocio.get_producto(producto_id)
        bodega = Negocio.get_bodega(bodega_id)
        stock_bodega = Negocio.get_stockBodega(producto,bodega)
        if (stock_bodega== None):
            stock_bodega =  ProductoCantidad(producto=producto,bodega=bodega,cantidad=cantidad)
        else:
            stock_bodega.cantidad=cantidad


        stock_bodega.save()

        return True

            
    def get_regionAll():
        try:
            return Region.objects.all()
        except Region.DoesNotExist:
            raise None    
            
    def get_region_nombre(nombre):
        try:
            return Region.objects.get(nombre=nombre)
        except Region.DoesNotExist:
            return None    
    def get_region(id):
        try:
            return Region.objects.get(id=id)
        except Region.DoesNotExist:
            return None         
  
    def regionCrear(nombre):
        region = Negocio.get_region_nombre(nombre)
        if (region==None):
            region = Region(nombre=nombre) 
        else:
            region.nombre

        region.save()
        return True
    
  

    def get_ciudadAll():
        try:
            return Ciudad.objects.all()
        except Ciudad.DoesNotExist:
            raise None    
            
    def get_ciudad_nombre(nombre):
        try:
            return Ciudad.objects.get(nombre=nombre)
        except Ciudad.DoesNotExist:
            return None
    def get_ciudad(id):
        try:
            return Ciudad.objects.get(id=id)
        except Ciudad.DoesNotExist:
            return None             
  
    def ciudadCrear(nombre,region_id):
        ciudad = Negocio.get_ciudad_nombre(nombre)
        if (ciudad==None):
            ciudad = Ciudad(nombre=nombre,region_id=region_id)
        else:
            ciudad.nombre=nombre
            ciudad.region_id=region_id
        ciudad.save()
        return True


    def crear_CompraProveedor(usuario,proveedor,producto,cantidad,bodega):
        usuario=Negocio.get_usuario(usuario)
        producto=Negocio.get_producto(id=producto)
        compra = ComprasProveedor(usuario=usuario,proveedor_id=proveedor,producto_id=producto,precio=producto.precio,cantidad=cantidad,bodega=bodega)
        compra.save()
        return True
   




