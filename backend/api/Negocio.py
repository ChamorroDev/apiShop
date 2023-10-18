from .models import *
class Negocio:
    def get_viewCliente( rut):
        try:
            # trampa
            # ViewCliente ==> declarada en la model, pero es una vista en la base de datos
            return ViewCliente.objects.get(pk=rut)
        except ViewCliente.DoesNotExist:
            raise None
        
    def get_viewClienteAll():
        try:
            # trampa
            # ViewCliente ==> declarada en la model, pero es una vista en la base de datos
            return ViewCliente.objects.all()
        except ViewCliente.DoesNotExist:
            raise None        

    def get_cliente( rut):
        try:
            return Cliente.objects.get(pk=rut)
        except Cliente.DoesNotExist:
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
            
    def clienteCrear(rut,dv,nombres,paterno,materno,email,telefono,genero):
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

        # No tienen mucho sentido solo es para el ejemplo
        if (cliente== None):
            cliente = Cliente(rut,None,'2023-01-01',0)
        if (usuario== None):
            usuario = Usuario(None,rut,rut,rut)
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
        ###  Recuerde que no debiera eliminar, mejor desactivar el registro
        usuario.delete()
        cliente.delete()
        persona.delete()          


class NegocioRegion:        
    def get_regionAll():
        try:
            return Region.objects.all()
        except Region.DoesNotExist:
            raise None    
            
    def get_region(id):
        try:
            return Region.objects.get(id=id)
        except Region.DoesNotExist:
            return None             
  
    def regionCrear(nombre):
        region =  Region(nombre=nombre)
        region.save()
        return True
    def get_region(id):
        try:
            return Region.objects.get(id=id)
        except Region.DoesNotExist:
            return None  
    def regionActualizar(id,nombre):
        region=NegocioRegion.get_region(id)
        region.nombre = nombre
        region.save()
        return True
    
    def regionGet(id):
        return NegocioRegion.get_region(id)

class NegocioCiudad:        
    def get_ciudadAll():
        try:
            return Ciudad.objects.all()
        except Ciudad.DoesNotExist:
            raise None    
            
    def get_ciudad(id):
        try:
            return Ciudad.objects.get(id=id)
        except Ciudad.DoesNotExist:
            return None             
  
    def ciudadCrear(nombre,region_id):
        region = Ciudad(nombre=nombre,region_id=region_id)
        region.save()
        return True
    def get_ciudad(id):
        try:
            return Ciudad.objects.get(id=id)
        except Ciudad.DoesNotExist:
            return None  
    def ciudadActualizar(id,nombre,region_id):
        ciudad=NegocioCiudad.get_ciudad(id)
        ciudad.nombre = nombre
        ciudad.region_id = region_id
        ciudad.save()
        return True
    
    def ciudadGet(id):
        return NegocioCiudad.get_ciudad(id)




