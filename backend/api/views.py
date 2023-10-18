from rest_framework import generics
from .models import *
from .serializers import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.middleware.csrf import get_token
from django.http import JsonResponse
from rest_framework.views import APIView
from .Negocio import *
from django.core import serializers
from django.core.exceptions import ValidationError
from rest_framework import status
from transbank.webpay.transaccion_completa.transaction import Transaction


class JSONResponseOkRows(HttpResponse):
    def __init__(self, data,msg, **kwargs):
        #print(len(data))
        data= {"OK":True,"count":len(data),"registro":data,"msg":msg}
        #print("data",data)
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOkRows, self).__init__(content, **kwargs)

class JSONResponseOk(HttpResponse):
    def __init__(self, data, msg,**kwargs):
        #print("data",data)
        data= {"OK":True,"count":"1","registro":data,"msg":msg}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOk, self).__init__(content, **kwargs)

class JSONResponseErr(HttpResponse):
    def __init__(self, data, **kwargs):
        data= {"OK":False,"count":"0","msg":data}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseErr, self).__init__(content, **kwargs)

class SucursalList(APIView):
    def get(self, request, format=None):
        SucursalLista = SucursalSerializer(Sucursal.objects.all(), many=True)
        RegionLista = RegionSerializer(Region.objects.all(), many=True)
        CiudadLista = CiudadSerializer(Ciudad.objects.all(), many=True)
        dataTodo = {
           
                'regSucursalList':SucursalLista.data,
                'regRegionList':RegionLista.data,
                'regCiudadesList':CiudadLista.data,

                }
        return JSONResponseOk(dataTodo,msg="Lista sucursales")
    


    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = SucursalSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="Sucursal Agregada")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class SucursalDetail(APIView):
    def get(self, request, id, format=None):
        SucursalLista = SucursalSerializer(Sucursal.objects.get(id=id))
        RegionLista = RegionSerializer(Region.objects.all(), many=True)
        CiudadLista = CiudadSerializer(Ciudad.objects.all(), many=True)
        dataTodo = {
           
                'regSucursalList':SucursalLista.data,
                'regRegionList':RegionLista.data,
                'regCiudadesList':CiudadLista.data,

                }
        return JSONResponseOk(dataTodo,msg="Detalle sucursal")
    
    def put(self, request, id, format=None):
        registro = Sucursal.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = SucursalSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="Sucursal Actualizada")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class RegionList(APIView):
    def get(self, request, format=None):
         registro = Region.objects.all()
         serializer = RegionSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = RegionSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="Region Agregada")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class RegionDetail(APIView):
    def get(self, request, id, format=None):
        registro = Region.objects.get(id=id)
        serializer = RegionSerializer(registro)
        return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = Region.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = RegionSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="Region Actualizada")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
    
class CiudadList(APIView):
    def get(self, request, format=None):
         registro = Ciudad.objects.all()
         serializer = CiudadSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = CiudadSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="Ciudad Agregada")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class CiudadDetail(APIView):
    def get(self, request, id, format=None):
            registro = Ciudad.objects.get(id=id)
            serializer = CiudadSerializer(registro)
            return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = Ciudad.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = CiudadSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="Ciudad Actualizada")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
    
class MarcaList(APIView):
    def get(self, request, format=None):
         registro = Marca.objects.all()
         serializer = MarcaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = MarcaSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="Marca Agregada")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class MarcaDetail(APIView):
    def get(self, request, id, format=None):
            registro = Marca.objects.get(id=id)
            serializer = MarcaSerializer(registro)
            return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = Marca.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = MarcaSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="Marca Actualizada")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
    
class GeneroList(APIView):
    def get(self, request, format=None):
         registro = Genero.objects.all()
         serializer = GeneroSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = GeneroSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="Genero Agregado")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class GeneroDetail(APIView):
    def get(self, request, id, format=None):
            registro = Genero.objects.get(id=id)
            serializer = GeneroSerializer(registro)
            return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = Genero.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = GeneroSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="Genero Actualizado")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
    
class CargoList(APIView):
    def get(self, request, format=None):
         registro = Cargo.objects.all()
         serializer = CargoSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = CargoSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="Cargo Agregado")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class CargoDetail(APIView):
    def get(self, request, id, format=None):
            registro = Cargo.objects.get(id=id)
            serializer = CargoSerializer(registro)
            return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = Cargo.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = CargoSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="Cargo Actualizado")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
   
class CategoriaList(APIView):
    def get(self, request, format=None):
         registro = Categoria.objects.all()
         serializer = CategoriaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = CategoriaSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="Categoria Agregada")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class CategoriaDetail(APIView):
    def get(self, request, id, format=None):
            registro = Categoria.objects.get(id=id)
            serializer = CategoriaSerializer(registro)
            return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = Categoria.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = CategoriaSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="Categoria Actualizada")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
   
class FormaPagoList(APIView):
    def get(self, request, format=None):
         registro = FormaPago.objects.all()
         serializer = FormaPagoSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = FormaPagoSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="FormaPago Agregada")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class FormaPagoDetail(APIView):
    def get(self, request, id, format=None):
            registro = FormaPago.objects.get(id=id)
            serializer = FormaPagoSerializer(registro)
            return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = FormaPago.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = FormaPagoSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="FormaPago Actualizada")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
   
class DireccionList(APIView):
    def get(self, request, format=None):
         registro = Direccion.objects.all()
         serializer = DireccionSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = DireccionSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="Direccion Agregada")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        
class DireccionListCliente(APIView):
    def get(self, request,id, format=None):
         registro = Direccion.objects.filter(cliente=id)
         serializer = DireccionSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")


class DireccionDetail(APIView):
    def get(self, request, id, format=None):
            registro = Direccion.objects.get(id=id)
            serializer = DireccionSerializer(registro)
            return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = Direccion.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = DireccionSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="Direccion Actualizada")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
  
class AtributoList(APIView):
    def get(self, request, format=None):
         registro = Atributo.objects.all()
         serializer = AtributoSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = AtributoSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="Atributo Agregada")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class AtributoDetail(APIView):
    def get(self, request, id, format=None):
            registro = Atributo.objects.get(id=id)
            serializer = AtributoSerializer(registro)
            return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = Atributo.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = AtributoSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="Atributo Actualizada")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
  
class ValorAtributoList(APIView):
    def get(self, request, format=None):
         registro = ValorAtributo.objects.all()
         serializer = ValorAtributoSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = ValorAtributoSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="ValorAtributo Agregado")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class ValorAtributoDetail(APIView):
    def get(self, request, id, format=None):
            registro = ValorAtributo.objects.get(id=id)
            serializer = ValorAtributoSerializer(registro)
            return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = Atributo.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = ValorAtributoSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="ValorAtributo Actualizado")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
  
class TarjetaList(APIView):
    def get(self, request, format=None):
         registro = Tarjeta.objects.all()
         serializer = TarjetaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = TarjetaSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="Tarjeta Agregada")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class TarjetaListCliente(APIView):
    def get(self, request,rut, format=None):
         registro = Tarjeta.objects.filter(cliente=rut)
         serializer = TarjetaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    
class TarjetaDetail(APIView):
    def get(self, request, id, format=None):
            registro = Tarjeta.objects.get(id=id)
            serializer = TarjetaSerializer(registro)
            return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = Tarjeta.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = TarjetaSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="Tarjeta Actualizada")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
  



###################### VISTAS NEGOCIO ######################
###################### VISTAS NEGOCIO ######################
###################### VISTAS NEGOCIO ######################
###################### VISTAS NEGOCIO ######################
###################### VISTAS NEGOCIO ######################

class ViewCategoriasMarcasAtributos(APIView):
    def get(self, request, format=None):
            dataCategoria = CategoriaSerializer(Categoria.objects.all(), many=True)
            dataMarca = MarcaSerializer(Marca.objects.all(), many=True)
            dataAtributo = AtributoSerializer(Atributo.objects.all(), many=True)

            dataTodo = {
                        'regCategoria':dataCategoria.data,
                        'regMarca':dataMarca.data,
                        'regAtributo':dataAtributo.data
                         }
            return JSONResponseOk(dataTodo,msg="Lista Categorias Marcas Atributos")
    

class CiudadesRegiones(APIView):
    def get(self, request, format=None):
            
            dataRegion = RegionSerializer(Region.objects.all(), many=True)
            dataCiudad = CiudadSerializer(Ciudad.objects.all(), many=True)
            dataTodo = {
                        'regRegion':dataRegion.data,
                        'regCiudad':dataCiudad.data
                         }
            return JSONResponseOk(dataTodo,msg="Lista Regiones Ciudades")
    
class ViewProductoList(APIView):
    def get(self, request, format=None):
            
            dataProducto = ProductoSerializer(Producto.objects.all(), many=True)


            dataTodo = {
                        'regProducto':dataProducto.data,
                         }
            return JSONResponseOk(dataTodo,msg="Lista productos")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        producto = data["producto"]
        atributos = data["atributos"]
        registro = Producto()
        registro.nombre = producto.get("nombre", registro.nombre)
        registro.descripcion = producto.get("descripcion", registro.descripcion)
        registro.marca = Marca.objects.get(id=int(producto["marca"]))
        registro.modelo = producto.get("modelo", registro.modelo)
        
        try:
            registro.full_clean()
        except ValidationError as e:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST, msg=str(e))
        registro.save()   

        for atributo in atributos:
            nombre_atributo = atributo.get("nombreAtributo")
            valor_atributo = atributo.get("valorAtributo")
            atributo_obj = Atributo.objects.get(nombre=nombre_atributo)
            valor_atributo_obj = ValorAtributo(valor=valor_atributo)
            valor_atributo_obj.save()
            tipo_producto_atributo = TipoProductoAtributo(
                atributo=atributo_obj,
                valorAtributo=valor_atributo_obj,
                producto=registro
            )
            tipo_producto_atributo.save()     
        categorias_ids = producto.get("categorias", [])
        for categoria_id in categorias_ids:
            try:
                categoria = Categoria.objects.get(id=categoria_id)
                registro.categorias.add(categoria)
            except Categoria.DoesNotExist:
                return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST, msg=f"Categoría con ID {categoria_id} no encontrada")

        return JSONResponseOk(None, msg="Producto Agregado")

        
class ViewProductoDetail(APIView):
    def get(self, request, ide, format=None):
            producto= Producto.objects.get(id=ide)
            dataMarcasList = MarcaSerializer(Marca.objects.all(), many=True)
            dataAtributosList = AtributoSerializer(Atributo.objects.all(), many=True)

            dataProducto = ProductoDetalleSerializer(producto)
            dataMarca = MarcaSerializer(Marca.objects.get(id=producto.marca.id))
            dataCategorias = CategoriaSerializer(producto.categorias.all(), many=True)
            tipo_producto_atributos = TipoProductoAtributo.objects.filter(producto=producto)

            dataCategoriasList = CategoriaSerializer(Categoria.objects.all(), many=True)
            tipo_producto_atributos_serializer = TipoProductoAtributoSerializer(tipo_producto_atributos, many=True)
            dataTodo = {
                        'regProducto':dataProducto.data,
                        'regMarcaDetail':dataMarca.data,
                        'regCategoriasDetail': dataCategorias.data,
                        'regTipoProductoAtributoDetail': tipo_producto_atributos_serializer.data,
                        'regMarcaList':dataMarcasList.data,
                        'regCategoriasList':dataCategoriasList.data,
                        'regAtributoList':dataAtributosList.data,
                         }
            return JSONResponseOk(dataTodo,msg="Detalle producto")
  
    def put(self, request, ide, format=None):
        registro = Producto.objects.get(id=ide)
        data = JSONParser().parse(request)
        producto = data["producto"]
        atributos = data["atributos"]
        registro.nombre = producto.get("nombre", registro.nombre)
        registro.descripcion = producto.get("descripcion", registro.descripcion)
        registro.marca = Marca.objects.get(id=int(producto["marca"]))
        registro.modelo = producto.get("modelo", registro.modelo)
        categorias_ids = producto.get("categorias", [])
        registro.categorias.clear()
        for categoria_id in categorias_ids:
            try:
                categoria = Categoria.objects.get(id=categoria_id)
                registro.categorias.add(categoria)
            except Categoria.DoesNotExist:
                return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST, msg=f"Categoría con ID {categoria_id} no encontrada")
        try:
            registro.full_clean()  
        except ValidationError as e:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST, msg=str(e))
        valor_ids_a_eliminar = TipoProductoAtributo.objects.filter(producto_id=registro.id)
        ids_a_eliminar = [tipo_producto_atributo.id for tipo_producto_atributo in valor_ids_a_eliminar]
        TipoProductoAtributo.objects.filter(producto=registro).delete()
        for valor in ids_a_eliminar:
            ValorAtributo.objects.filter(id=int(valor)).delete()
        for atributo in atributos:
            nombre_atributo = atributo.get("nombreAtributo")
            valor_atributo = atributo.get("valorAtributo")
            try:
                atributo_obj = Atributo.objects.get(nombre=nombre_atributo)
            except Atributo.DoesNotExist:
                atributo_obj = Atributo(nombre=nombre_atributo)
                atributo_obj.save()
            try:
                valor_atributo_obj = ValorAtributo.objects.get(valor=valor_atributo)
            except ValorAtributo.DoesNotExist:
                valor_atributo_obj = ValorAtributo(valor=valor_atributo)
                valor_atributo_obj.save()
            tipo_producto_atributo = TipoProductoAtributo(
                atributo=atributo_obj,
                valorAtributo=valor_atributo_obj,
                producto=registro
            )
            tipo_producto_atributo.save()
        registro.save()  
        return JSONResponseOk(None, msg="Producto Actualizado")
  
 
    
class ClienteList(APIView):

    def get(self, request, format=None):
         registro = Negocio.get_viewClienteAll()
         serializer = ViewClienteSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if (not Negocio.clienteCrear(data['rut'],data['dv']
                            ,data['nombre'],data['appaterno'],data['apmaterno']
                            ,data['email']
                            ,data['telefono']
                            ,data['genero'])):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None,msg="Registro Actualizado")

class ClienteDetail(APIView):
    
    def get(self, request, rut, format=None):
        registro = Negocio.clienteGet(rut)
        serializer = ViewClienteSerializer(registro)
        return JSONResponseOk(serializer.data,msg="")  
    
    # No es necesario ya que el Negocio.clienteCrear, actualiza o crea
    # debe cambiarlo según sus necesidades

    # def put(self, request, rut, format=None):
    #     data = JSONParser().parse(request)
    #     if (not Negocio.clienteActualizar(rut,data['dv']
    #                         ,data['nombre'],data['papellido'],data['sapellido']
    #                         ,data['email']
    #                         ,data['comuna'],data['genero'])):
    #         return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
    #     return JSONResponseOk(None,msg="Resistro Actualizado")

    def delete(self, request, rut, format=None):
        data = JSONParser().parse(request)
        if (not Negocio.clienteEliminar(rut)):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None,msg="Resistro Actualizado")
    
def get_retiro_persona( rut):
        try:
            return RetiroPersona.objects.get(rut=rut)
        except RetiroPersona.DoesNotExist:
            return None 
class CarritoSucursal(APIView):
     def post(self, request,format=None):
        data = JSONParser().parse(request)
        cliente=Cliente.objects.get(rut=data['rut'])
        if 'sucursal' in data:
            sucursal=Sucursal.objects.get(id=data['sucursal'])
            carros=Carrito.objects.filter(cliente=cliente)
            for carro in carros:
                carro.sucursal=sucursal
                carro.retiroPersona=None

                carro.save()

            return JSONResponseOk(data,msg="Sucursal añadida al carro")
        if 'retiraRUT' in data:
            carros=Carrito.objects.filter(cliente=cliente)
            retiro=get_retiro_persona(data['retiraRUT'])
            if retiro is None:
                retiro=RetiroPersona(rut=data['retiraRUT'] , dv=data['dv'], nombre=data['nombre'], apellido=data['apellido'])
                retiro.save()
                for carro in carros:
                    carro.retiroPersona=retiro
                    carro.direccion=None
                    carro.save()
                return JSONResponseOk(data,msg="Persona que retira añadida no existe la persona")
            
            else:
                for carro in carros:
                    carro.retiroPersona=retiro
                    carro.save()
                    return JSONResponseOk(data,msg="Persona que retira añadida existente")
        if 'Direccion_id' in data:
            carros=Carrito.objects.filter(cliente=cliente)
            dir=Direccion.objects.get(id=data['Direccion_id'])
            for carro in carros:
                    carro.direccion=dir
                    carro.sucursal=None
                    carro.save()
            return JSONResponseOk(data,msg="Agregado direccion al carro")

        else:
            return JSONResponseOk(data,msg="no existe nada")
     
class CarroCliente(APIView):
    
    def get(self, request, rut, format=None):
        carritos = Carrito.objects.filter(cliente=rut)
        serializer = CarritoSerializer(carritos, many=True)
        dataTodo = {
            'regProducto': serializer.data,
        }
        return JSONResponseOk(dataTodo,msg="Listado del carrito")
    def post(self, request,rut,format=None):
        data = JSONParser().parse(request)
        cliente=Cliente.objects.get(rut=rut)
        Carrito.objects.filter(cliente=cliente).delete()
        for elem in data['productos']:
            producto=Producto.objects.get(id=elem['producto'])

            if data['documento'] == 'Boleta':
                if data['envio'] == 'Direccion':
                    carro=Carrito(cantidad=elem['cantidad'],cliente=cliente,producto=producto,documento= 'Boleta',envio="Direccion")
                if data['envio'] == 'Sucursal':
                    carro=Carrito(cantidad=elem['cantidad'],cliente=cliente,producto=producto,documento= 'Boleta',envio="Sucursal")

            if data['documento'] == 'Factura':
                if data['envio'] == 'Direccion':
                    carro=Carrito(cantidad=elem['cantidad'],cliente=cliente,producto=producto,documento= 'Factura',envio="Direccion")

                if data['envio'] == 'Sucursal':
                    carro=Carrito(cantidad=elem['cantidad'],cliente=cliente,producto=producto,documento= 'Factura',envio="Sucursal")
            
            carro.save()

        return JSONResponseOk(data,msg="no existe, se agrega al carro")


    def delete(self, request,rut, format=None):
 
        cli=Cliente.objects.get(rut=rut)
        carro=Carrito.objects.filter(cliente=cli)
        carro.delete()
        return JSONResponseOk(None,msg="Producto borrado del carro")

class CarroClientePost(APIView):
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        prod=Producto.objects.get(id=data['producto'])
        cli=Cliente.objects.get(rut=data['cliente'])
        
        if Carrito.objects.filter(cliente=data['cliente'], producto=prod).count() == 0:
            carro = Carrito( producto=prod,cliente=cli, cantidad=data['cantidad'])
            carro.save()

            return JSONResponseOk(data,msg="no existe, se agrega al carro")

       
        carro=Carrito.objects.get(cliente=data['cliente'], producto=prod)
        print (carro.cantidad)
        carro.cantidad=data['cantidad']+carro.cantidad
        carro.save()
        return JSONResponseOk(data,msg="Si existe, se cambia al cantidad")
        
from transbank.error.transbank_error import TransbankError
class CrearWebPay(APIView):
    def post(self, request,format=None):
        try:
            ####3 CREO EL PEDIDO ADEMAS EN ESTADO NO PAGADO Y TODAS LAS DEMAS VARIABLES
            total=123
            orden_compra = '1231'
            return_url= 'http://localhost:8000/folder/'
            s_id='1231'

            ##response = (Transaction()).create(orden_compra, s_id, total, return_url)
            ##print (response)
            data = JSONParser().parse(request)
            tar=data['tarjeta']


            tarjeta=Tarjeta.objects.get(id=tar['id'])
            card_number =str(tarjeta.numero)

            cvv = str(tarjeta.csv)

            card_expiration_date = str(tarjeta.annovenc)+'/'+str(tarjeta.mesvenc)

            # Crear la transacción
            resp_create = Transaction().create(buy_order=orden_compra, session_id=s_id, amount=total, cvv=cvv, card_number=card_number, card_expiration_date=card_expiration_date)

            if 'token' in resp_create:
                token = resp_create['token']
        

                resp_status = Transaction().status(token=token)

                print(resp_status)
            else:
                print("Error al crear la transacción: ", resp_create)  


        
            grace_period = 0
            id_query_installments = "id1" 
            deferred_period_index = 0 
            tx = Transaction()
            resp = tx.installments(token=token, installments_number=2)#cuota***********
            try:
                resp_commit = Transaction().commit(token=token, id_query_installments=resp['id_query_installments'], deferred_period_index=deferred_period_index, grace_period=grace_period)

                if 'response_code' in resp_commit and resp_commit['response_code'] == 0:
                    print("Transacción confirmada exitosamente.")
                else:
                    print(f"Error al confirmar la transacción: {resp_commit.get('response_code', 'Desconocido')} - {resp_commit.get('error_message', 'Mensaje de error no proporcionado')}")
            except TransbankError as e:
                print(f"Error al confirmar la transacción: {e.code} - {e.message}")  
            resp_status = Transaction().status(token=token)
            dataTodo = {
                            'respuesta':resp_status
                            }
            return JSONResponseOk(dataTodo,msg="Termino bien")
        except Exception as e:
            print(f"Error al confirmar la transacción: {e.code} - {e.message}")  

            dataTodo = {
                            'respuesta':'Error',
                            'error':e
                            }
            return JSONResponseOk(dataTodo,msg="No se realizo el pagó!")




############## END VISTAS NEGOCIO ######################
###################### END VISTAS NEGOCIO ######################
###################### END VISTAS NEGOCIO ######################
###################### END VISTAS NEGOCIO ######################
###################### END VISTAS NEGOCIO ######################
@csrf_exempt
def obtener_token_csrf(request):
    token = get_token(request)
    return JsonResponse({'csrf_token': token})

class JSONResponse(HttpResponse):
   
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def ListaCategorias(request):
    if request.method == 'GET':
         registro = Categoria.objects.all()
         serializer = CategoriaSerializer(registro, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
         data = JSONParser().parse(request)
         registro = CategoriaSerializer(data=data)
         if registro.is_valid():
              registro.save()
              return JSONResponse(registro.data, status=201)
         
    return JSONResponse(registro.errors, status=400) 

@csrf_exempt
def DetalleCategoria(request, id):
    try:
        registro = Categoria.objects.get(id=id)
    except Categoria.DoesNotExist:
        return HttpResponse(status=408)  

    if request.method == 'GET':
        registro = CategoriaSerializer(registro)
        return JSONResponse(registro.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        registro_serializer = CategoriaSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponse(registro_serializer.data)

    return JSONResponse(registro.errors, status=400)



@csrf_exempt
def ListaProductos(request):
    if request.method == 'GET':
         registro = Producto.objects.all()
         serializer = ProductoSerializer(registro, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        registro = ProductoSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponse(registro.data, status=201)
        else:
            errors = registro.errors
            print(errors)
            
        return JSONResponse(registro.errors, status=400) 

@csrf_exempt
def DetalleProducto(request, id):
    try:
        registro = Producto.objects.get(id=id)
    except Producto.DoesNotExist:
        return HttpResponse(status=408)  

    if request.method == 'GET':
        registro = ProductoSerializer(registro)
        return JSONResponse(registro.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        registro_serializer = ProductoSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponse(registro_serializer.data)

    return JSONResponse(registro.errors, status=400)


@csrf_exempt
def ListaEmpleados(request):
    if request.method == 'GET':
         registro = Empleado.objects.all()
         serializer = EmpleadoSerializer(registro, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        registro = EmpleadoSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponse(registro.data, status=201)
        else:
            errors = registro.errors
            print(errors)
            
        return JSONResponse(registro.errors, status=400) 

@csrf_exempt
def DetalleEmpleado(request, id):
    try:
        registro = Empleado.objects.get(id=id)
    except Empleado.DoesNotExist:
        return HttpResponse(status=408)  

    if request.method == 'GET':
        registro = EmpleadoSerializer(registro)
        return JSONResponse(registro.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        registro_serializer = EmpleadoSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponse(registro_serializer.data)

    return JSONResponse(registro.errors, status=400)


@csrf_exempt
def ListaMovimientoBodegas(request):
    if request.method == 'GET':
         registro = MovimientoBodega.objects.all()
         serializer = MovimientoBodegaSerializer(registro, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        registro = MovimientoBodegaSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponse(registro.data, status=201)
        else:
            errors = registro.errors
            print(errors)
            
        return JSONResponse(registro.errors, status=400) 

@csrf_exempt
def DetalleMovimientoBodegas(request, id):
    try:
        registro = MovimientoBodega.objects.get(id=id)
    except MovimientoBodega.DoesNotExist:
        return HttpResponse(status=408)  

    if request.method == 'GET':
        registro = MovimientoBodegaSerializer(registro)
        return JSONResponse(registro.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        registro_serializer = MovimientoBodegaSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponse(registro_serializer.data)

    return JSONResponse(registro.errors, status=400)

@csrf_exempt
def ListaSucursales(request):
    if request.method == 'GET':
         registro = Sucursal.objects.all()
         serializer = SucursalSerializer(registro, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        registro = SucursalSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponse(registro.data, status=201)
        else:
            errors = registro.errors
            print(errors)
            
        return JSONResponse(registro.errors, status=400) 

@csrf_exempt
def DetalleSucursal(request, id):
    try:
        registro = Sucursal.objects.get(id=id)
    except Sucursal.DoesNotExist:
        return HttpResponse(status=408)  

    if request.method == 'GET':
        registro = SucursalSerializer(registro)
        return JSONResponse(registro.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        registro_serializer = SucursalSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponse(registro_serializer.data)

    return JSONResponse(registro.errors, status=400)


@csrf_exempt
def ListaRegiones(request):
    if request.method == 'GET':
         registro = Region.objects.all()
         serializer = RegionSerializer(registro, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        registro = RegionSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponse(registro.data, status=201)
        else:
            errors = registro.errors
            print(errors)
            
        return JSONResponse(registro.errors, status=400) 

@csrf_exempt
def DetalleRegion(request, id):
    try:
        registro = Region.objects.get(id=id)
    except Region.DoesNotExist:
        return HttpResponse(status=408)  

    if request.method == 'GET':
        registro = RegionSerializer(registro)
        return JSONResponse(registro.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        registro_serializer = RegionSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponse(registro_serializer.data)

    return JSONResponse(registro.errors, status=400)


@csrf_exempt
def ListaCiudades(request):
    if request.method == 'GET':
         registro = Ciudad.objects.all()
         serializer = CiudadSerializer(registro, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        registro = CiudadSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponse(registro.data, status=201)
        else:
            errors = registro.errors
            print(errors)
            
        return JSONResponse(registro.errors, status=400) 

@csrf_exempt
def DetalleCiudad(request, id):
    try:
        registro = Ciudad.objects.get(id=id)
    except Ciudad.DoesNotExist:
        return HttpResponse(status=408)  

    if request.method == 'GET':
        registro = CiudadSerializer(registro)
        return JSONResponse(registro.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        registro_serializer = CiudadSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponse(registro_serializer.data)

    return JSONResponse(registro.errors, status=400)


@csrf_exempt
def ListaBodegas(request):
    if request.method == 'GET':
         registro = Bodega.objects.all()
         serializer = BodegaSerializer(registro, many=True)
         return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        registro = BodegaSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponse(registro.data, status=201)
        else:
            errors = registro.errors
            print(errors)
            
        return JSONResponse(registro.errors, status=400) 

@csrf_exempt
def DetalleBodega(request, id):
    try:
        registro = Bodega.objects.get(id=id)
    except Bodega.DoesNotExist:
        return HttpResponse(status=408)  

    if request.method == 'GET':
        registro = BodegaSerializer(registro)
        return JSONResponse(registro.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        registro_serializer = BodegaSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponse(registro_serializer.data)

    return JSONResponse(registro.errors, status=400)
