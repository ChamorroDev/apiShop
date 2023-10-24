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
from transbank.error.transbank_error import TransbankError
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.storage import default_storage
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

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

class EmpleadoList(APIView):
    def get(self, request, format=None):
         registro = Empleado.objects.all()
         serializer = EmpleadoSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = EmpleadoSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="Empleado Agregada")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class EmpleadoDetail(APIView):
    def get(self, request, id, format=None):
            registro = Empleado.objects.get(id=id)
            serializer = EmpleadoSerializer(registro)
            return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = Empleado.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = EmpleadoSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="Empleado Actualizada")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)


class ProveedorList(APIView):
    def get(self, request, format=None):
         registro = Proveedor.objects.all()
         serializer = ProveedorSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = ProveedorSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="Proveedor Agregada")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class ProveedorDetail(APIView):
    def get(self, request, id, format=None):
            registro = Proveedor.objects.get(id=id)
            serializer = ProveedorSerializer(registro)
            return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = Proveedor.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = ProveedorSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="Proveedor Actualizada")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class BodegaList(APIView):
    def get(self, request, format=None):
        BodegaLista = BodegaSerializer(Bodega.objects.all(), many=True)
        RegionLista = RegionSerializer(Region.objects.all(), many=True)
        CiudadLista = CiudadSerializer(Ciudad.objects.all(), many=True)
        dataTodo = {
           
                'regBodegaList':BodegaLista.data,
                'regRegionList':RegionLista.data,
                'regCiudadesList':CiudadLista.data,

                }
        return JSONResponseOk(dataTodo,msg="Lista bodegas")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = BodegaSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="agregada bodegas")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class BodegaDetail(APIView):
    def get(self, request, id, format=None):
        BodegaLista = BodegaSerializer(Bodega.objects.get(id=id))
        RegionLista = RegionSerializer(Region.objects.all(), many=True)
        CiudadLista = CiudadSerializer(Ciudad.objects.all(), many=True)
        dataTodo = {
           
                'regBodegaList':BodegaLista.data,
                'regRegionList':RegionLista.data,
                'regCiudadesList':CiudadLista.data,

                }
        return JSONResponseOk(dataTodo,msg="Detalle bodegas")
    
    def put(self, request, id, format=None):
        registro = Bodega.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = BodegaSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="actualizada bodegas")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

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
  
class FacturaList(APIView):
    def get(self, request, format=None):
         registro = Factura.objects.all()
         serializer = FacturaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = FacturaSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="Factura Agregado")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class FacturaDetail(APIView):
    def get(self, request, id, format=None):
            registro = Factura.objects.get(id=id)
            serializer = FacturaSerializer(registro)
            return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = Factura.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = FacturaSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="Factura Actualizado")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class BoletaList(APIView):
    def get(self, request, format=None):
         registro = Boleta.objects.all()
         serializer = BoletaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        registro = BoletaSerializer(data=data)
        if registro.is_valid():
            registro.save()
            return JSONResponseOk(None,msg="Boleta Agregado")
        else:
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)

class BoletaDetail(APIView):
    def get(self, request, id, format=None):
            registro = Boleta.objects.get(id=id)
            serializer = BoletaSerializer(registro)
            return JSONResponseOk(serializer.data,msg="")  
    def put(self, request, id, format=None):
        registro = Boleta.objects.get(id=id)
        data = JSONParser().parse(request)
        registro_serializer = BoletaSerializer(registro, data=data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JSONResponseOk(None,msg="Boleta Actualizado")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
    


class ciudadtest(APIView):
    def get(self, request, format=None):
         registro = Negocio.get_ciudadAll()
         serializer = CiudadSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if Negocio.ciudadCrear(data['nombre'], data['region_id']):
                return JSONResponseOk(None,msg="ciudad cambiada")
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
            # Crear una imagen de prueba
            """
            image = Image.new('RGB', (100, 100), color='red')
            image_file = BytesIO()
            image.save(image_file, 'png')
            image_file.seek(0)
            producto=Producto.objects.get(id=1)
            foto_producto = FotoProducto(producto=producto)
            foto_producto.foto.save('test_image.png', File(image_file))
            producto.save()
            foto_producto.save()
            """


            dataProducto = ProductoSerializer(Producto.objects.all(), many=True, context={'request': request})

            
            dataTodo = {
                        'regProducto':dataProducto.data,
                         }
            return JSONResponseOk(dataTodo,msg="Lista productos")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        producto = data["producto"]
        atributos = data["atributos"]
        fotos = data["foto"]

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
        i=0
        for foto in fotos:
            
           
            image_data = foto
            format, imgstr = image_data.split(';base64,')  
            ext = format.split('/')[-1]  
            image_data = base64.b64decode(imgstr)
            
            nombre_archivo = f'producto_{i}_foto.{ext}'
            foto_producto = FotoProducto(producto=registro, foto=nombre_archivo)
            foto_producto.foto.save(nombre_archivo, ContentFile(image_data))
            foto_producto.save()
            i += 1
    

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
                print("hola")
                return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST, msg=f"Categoría con ID {categoria_id} no encontrada")

        return JSONResponseOk(None, msg="Producto Agregado")

        
class ViewProductoDetail(APIView):
    def get(self, request, ide, format=None):
            producto= Producto.objects.get(id=ide)
            dataMarcasList = MarcaSerializer(Marca.objects.all(), many=True)
            dataAtributosList = AtributoSerializer(Atributo.objects.all(), many=True)
            dataFotos= FotoProducto.objects.filter(producto=producto)
            dataProducto = ProductoDetalleSerializer(producto)
            dataMarca = MarcaSerializer(Marca.objects.get(id=producto.marca.id))
            dataCategorias = CategoriaSerializer(producto.categorias.all(), many=True)
            tipo_producto_atributos = TipoProductoAtributo.objects.filter(producto=producto)


            dataFotosList = FotoProductoSerializer(dataFotos, many=True, context={'request': request})

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
                        'dataFotos':dataFotosList.data,

                         }
            return JSONResponseOk(dataTodo,msg="Detalle producto")
  
    def put(self, request, ide, format=None):
        registro = Producto.objects.get(id=ide)
        data = JSONParser().parse(request)
        producto = data["producto"]
        atributos = data["atributos"]
        fotos = data["fotos"]

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
            valor_atributo_obj = ValorAtributo(valor=valor_atributo)
            valor_atributo_obj.save()
            atributo_obj = Atributo.objects.get(nombre=nombre_atributo)
            tipo_producto_atributo = TipoProductoAtributo(
                atributo=atributo_obj,
                valorAtributo=valor_atributo_obj,
                producto=registro
            )
            tipo_producto_atributo.save()
        registro.save()  
        i=0
        FotoProducto.objects.filter(producto=registro).delete()

        for foto in fotos:
            foto_producto = FotoProducto(producto=registro)
            image_data =foto
            format, imgstr = image_data.split(';base64,')  
            ext = format.split('/')[-1]  
            image_data = base64.b64decode(imgstr)
            
            nombre_archivo = f'producto_{i}_foto.{ext}'
            foto_producto.foto.save(nombre_archivo, ContentFile(image_data))
            foto_producto.save
            i=i+1
            
        return JSONResponseOk(None, msg="Producto Actualizado")
  
 
class CambiarClaveUsuario(APIView):
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if Negocio.cambiarClave(data['rut'], data['clave']):
                return JSONResponseOk(None,msg="Clave cambiada")
        return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        


class ProductoProveedorList(APIView):

    def get(self, request, format=None):
         registro = Negocio.get_productoProveedorAll()
         serializer = ProductoProveedorSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if (not Negocio.crear_ProductoProveedor(data['id'],data['producto'],data['precio'])):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
 
        return JSONResponseOk(None,msg="producto proveedor actualizado")


class ProductoProveedorDetail(APIView):
    
    def get(self, request, rut, format=None):
        registro = Negocio.clienteGet(rut)
        serializer = ProductoProveedorSerializer(registro, context={'request': request})  # Pasar el contexto al serializador
        return JSONResponseOk(serializer.data,msg="")  

    def delete(self, request, rut, format=None):
        data = JSONParser().parse(request)
        if (not Negocio.clienteEliminar(rut)):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None,msg="producto proveedor Actualizado")
    

class PedidoList(APIView):
    def get(self, request, format=None):
        dataBoleta = BoletaSerializer(Boleta.objects.filter(), many=True)
        dataFactura = FacturaSerializer(Factura.objects.filter(), many=True)
        dataTodo = {
                    'boletas':dataBoleta.data,
                    'facturas':dataFactura.data,
                        }
        return JSONResponseOk(dataTodo,msg="todas las boletas y facturas")
    
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if (not Negocio.clienteCrear(data['rut'],data['dv']
                            ,data['nombre'],data['appaterno'],data['apmaterno']
                            ,data['email']
                            ,data['telefono']
                            ,data['genero']
                            ,data['foto'])):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        if ( 'clave' in data):
            print ("entre")
        return JSONResponseOk(None,msg="registro actualizado")
    

class ClienteList(APIView):

    def get(self, request, format=None):
         registro = Negocio.get_viewClienteAll()
         serializer = ViewClienteSerializer(registro, many=True, context={'request': request})
         return JSONResponseOkRows(serializer.data,"")

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if (not Negocio.clienteCrear(data['rut'],data['dv']
                            ,data['nombre'],data['appaterno'],data['apmaterno']
                            ,data['email']
                            ,data['telefono']
                            ,data['genero']
                            ,data['foto'])):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        if ( 'clave' in data):
            print ("entre")
        return JSONResponseOk(None,msg="registro actualizado")


class ClienteDetail(APIView):
    
    def get(self, request, rut, format=None):
        registro = Negocio.clienteGet(rut)
        serializer = ViewClienteSerializer(registro, context={'request': request})  # Pasar el contexto al serializador
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
        print (data)
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
     

class RetiradorCliente(APIView):
    def post(self, request,format=None):
        data = JSONParser().parse(request)
        print (data)
        cliente=Cliente.objects.get(rut=data['rut'])
        print (cliente.rut)
        carrito=Carrito.objects.filter(cliente=cliente)
        persona=RetiroPersona(data['retiraRUT'],data['dv'],data['nombre'],data['apellido'])
        
        persona.save()
        print(persona.nombre)
        for producto in carrito:
            producto.retiroPersona=persona
            producto.save()
            print(producto.retiroPersona.nombre)


        return JSONResponseOk(data,msg="no existe, se agrega al carro")


class CarroCliente(APIView):
    
    def get(self, request, rut, format=None):
        carritos = Carrito.objects.filter(cliente=rut)
        serializer = CarritoSerializer(carritos, many=True)
        fotos_url=[]
        for carrito in carritos:
            primer_foto = carrito.producto.fotos.first()  

            if primer_foto:
                
                fotos_url.append(request.build_absolute_uri(primer_foto.foto.url))

        dataTodo = {
            'regProducto': serializer.data,
            'regFotos':fotos_url
        }
        return JSONResponseOk(dataTodo,msg="Listado del carrito")
    def post(self, request,rut,format=None):
        data = JSONParser().parse(request)    
        fac = data.get('personaFactura')
        if fac['rut']!=None:
            razon = personaFactura.objects.create(rut=fac['rut'],  dv=fac['dv'], nombre=fac['nombre'], direccion=fac['direccion'], numero=fac['numero'])
            razon.save()
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
            if fac['rut']!=None:
                carro.razonFactura=razon
            else:
                carro.razonFactura=None
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
        
class CrearWebPay(APIView):
    def post(self, request,format=None):
        data = JSONParser().parse(request)
        tar=data['tarjeta']
        cli=Cliente.objects.get(rut=data['rut'])
        
       

        try:
            ####3 CREO EL PEDIDO ADEMAS EN ESTADO NO PAGADO Y TODAS LAS DEMAS VARIABLES
            total=123
            orden_compra = '1231'
            return_url= 'http://localhost:8000/folder/'
            s_id='1231'

            ##response = (Transaction()).create(orden_compra, s_id, total, return_url)
            ##print (response)
            


            tarjeta=Tarjeta.objects.get(id=tar['id'])
            card_number =str(tarjeta.numero)
            cvv = str(tarjeta.csv)
            card_expiration_date = str(tarjeta.annovenc)+'/'+str(tarjeta.mesvenc)

            # Crear la transacción
            resp_create = Transaction().create(buy_order=orden_compra, session_id=s_id, amount=total, cvv=cvv, card_number=card_number, card_expiration_date=card_expiration_date)

            if 'token' in resp_create:
                token = resp_create['token']
                resp_status = Transaction().status(token=token)
     
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
            except Exception as e:
                carrito= Carrito.objects.filter(cliente=cli) 
                for carro in carrito:
                    carro.error=e.message
                    carro.save()

                data = {
                                'respuesta':'Error',
                                'error':e.message
                                }
                return JSONResponseOk(data,msg="No se realizo el pagó!")
            resp_status = Transaction().status(token=token)
            dataTodo = {
                            'respuesta':resp_status
                            }
            


            ####CREACION DE BOLETA-FACTURA
            carrito= Carrito.objects.filter(cliente=cli) 
            for carro in carrito:
                carro.error="Sin errores"
                carro.save()
            primer_producto =carrito.first()

            if primer_producto.documento=="Boleta":
                boleta=Boleta()
                boleta.cliente=cli
                if primer_producto.envio=="Direccion":
                    boleta.direccion=primer_producto.direccion
                    boleta.tipoDespacho= TipoDespacho.objects.get(id=2) 
                    boleta.forma_pago= FormaPago.objects.get(id=1) 
                    boleta.estadoPedido= EstadoPedido.objects.get(id=10)

                if primer_producto.envio=="Sucursal":
                    boleta.sucursal=primer_producto.sucursal
                    boleta.retiroPersona=primer_producto.retiroPersona
                    boleta.tipoDespacho= TipoDespacho.objects.get(id=1) 
                    boleta.forma_pago= FormaPago.objects.get(id=1) 
                    boleta.estadoPedido= EstadoPedido.objects.get(id=10)
                    boleta.retiroPersona=primer_producto.retiroPersona
                boleta.precio_total=0
                boleta.save()
                total=0
                for producto in carrito :
                    detalle=DetalleBoleta()
                    detalle.boleta=boleta
                    prod=Producto.objects.get(id=producto.producto.id) 
                    detalle.producto=prod
                    detalle.cantidad=producto.cantidad
                    detalle.precio_unitario=prod.precio
                    detalle.subtotal=prod.precio*producto.cantidad
                    total=total+detalle.subtotal
                    detalle.save()

                boleta.precio_total=total
                boleta.save()
                carrito.delete()
            if primer_producto.documento=="Factura":
                factura=Factura()
                factura.cliente=cli
                factura.personaFactura=primer_producto.razonFactura
                if primer_producto.envio=="Direccion":
                    factura.direccion=primer_producto.direccion
                    factura.tipoDespacho= TipoDespacho.objects.get(id=2) 
                    factura.forma_pago= FormaPago.objects.get(id=1) 
                    factura.estadoPedido= EstadoPedido.objects.get(id=10)

                if primer_producto.envio=="Sucursal":
                    factura.sucursal=primer_producto.sucursal
                    factura.retiroPersona=primer_producto.retiroPersona
                    factura.tipoDespacho= TipoDespacho.objects.get(id=1) 
                    factura.forma_pago= FormaPago.objects.get(id=1) 
                    factura.estadoPedido= EstadoPedido.objects.get(id=10)
                    
                factura.precio_total=0
                factura.save()
                total=0
                for producto in carrito :
                    detalle=DetalleFactura()
                    detalle.factura=factura
                    prod=Producto.objects.get(id=producto.producto.id) 
                    detalle.producto=prod
                    detalle.cantidad=producto.cantidad
                    detalle.precio_unitario=prod.precio
                    detalle.subtotal=prod.precio*producto.cantidad
                    total=total+detalle.subtotal
                    detalle.save()

                factura.precio_total=total
                factura.save()
                carrito.delete()




            return JSONResponseOk(dataTodo,msg="Termino bien")
        
        except Exception as e:
            data = {
                            'respuesta':'Error',
                            'error':e
                    
                            }
            return JSONResponseOk(data,msg="No se realizo el pagó!")


class errorPago(APIView):
    def post(self, request,format=None):
        data = JSONParser().parse(request)
        cli=Cliente.objects.get(rut=data['rut'])
        carrito= Carrito.objects.filter(cliente=cli) 
        data = {
                'error':carrito[1].error
                }
        return JSONResponseOk(data,msg="")
    
from rest_framework_simplejwt.views import TokenObtainPairView
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):

        usuario_name = request.data.get('username')
        password = request.data.get('password')
        info=""
        print (usuario_name)
        if usuario_name is None or password is None:
            print ("if")

            return JSONResponseOk(info,msg='error Credenciales inválidas')
        
        try:
            print ("try")

            usuario = Usuario.objects.get(usuario=usuario_name,clave=password)

        except Usuario.DoesNotExist:
            print ("exc")

            return JSONResponseOk(info,msg='error Credenciales inválidas try')
        
        print ("info")

        info={'id': usuario.id,
            'access':  (CustomTokenObtainPairView, self).post(request, *args, **kwargs).data['access']

        }
        return JSONResponseOk(info,msg='Todo correcto')
    
from rest_framework_simplejwt.tokens import RefreshToken
class LoginView(APIView):
     def post(self, request):
        usuario_name = request.data.get('username')
        password = request.data.get('password')
        info="error"
        if usuario_name is None or password is None:
            return JSONResponseOk(info,msg='error')
        try:
            usuario = Usuario.objects.get(usuario=usuario_name,clave=password)
        except Usuario.DoesNotExist:
            return JSONResponseOk(info,msg='error')
        refresh = RefreshToken.for_user(usuario)
        access_token = str(refresh.access_token)
      
        info={
            'access_token': access_token ,
            'username': usuario_name,
            'rut':usuario.rut.rut

        }
        
        return JSONResponseOk(info,msg='Todo correcto')



       

############## END VISTAS NEGOCIO ######################
###################### END VISTAS NEGOCIO ######################
###################### END VISTAS NEGOCIO ######################
###################### END VISTAS NEGOCIO ######################
###################### END VISTAS NEGOCIO ######################
@csrf_exempt
def obtener_token_jwt(request):
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















