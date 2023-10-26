from rest_framework import serializers
from .models import *

class PersonaEmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        exclude = ['actived', 'edited', 'created']

class CargoEmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        exclude = ['actived', 'edited', 'created']

class EmpleadoEmpSerializer(serializers.ModelSerializer):
    rut = PersonaEmpSerializer()
    codCargo = CargoEmpSerializer()

    class Meta:
        model = Empleado
        fields = '__all__'


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'


class ProductoProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoProveedor
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'



class ViewClienteSerializer(serializers.ModelSerializer):
    ciudad_nombre = serializers.SerializerMethodField()
    genero_nombre = serializers.SerializerMethodField()
    nacimiento = serializers.SerializerMethodField()
    telefono = serializers.SerializerMethodField()
    foto = serializers.SerializerMethodField()

    class Meta:
        model = ViewCliente
        fields = ('usuario','rut', 'dv',  'nombre', 'appaterno', 'apmaterno', 'email','ciudad_nombre','genero_nombre','telefono','nacimiento','genero','foto')
    def get_foto(self, obj):
        try:
            cliente = Cliente.objects.get(rut_id=obj.rut)
            if cliente.foto:
                request = self.context.get('request')
                photo_url = cliente.foto.url
            
                return request.build_absolute_uri(photo_url)
            else:
                return None
        except Cliente.DoesNotExist:
            return None
    def get_ciudad_nombre(self, obj):
        try:
            ciudad_obj = Ciudad.objects.get(id=obj.ciudad.id)
            return ciudad_obj.nombre
        except Ciudad.DoesNotExist:
            return None

    def get_genero_nombre(self, obj):
        try:
            genero_obj = Genero.objects.get(id=obj.genero.id)
            return genero_obj.name
        except Genero.DoesNotExist:
            return None
    def get_nacimiento(self, obj):
        try:
            nacimiento = Persona.objects.get(rut=obj.rut)
            return nacimiento.fechaNacimiento
        except Persona.DoesNotExist:
            return None
    def get_telefono(self, obj):
        try:
            telefono = Persona.objects.get(rut=obj.rut)
            return telefono.telefono
        except Persona.DoesNotExist:
            return None

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class FotoProductoSerializer(serializers.ModelSerializer):
    foto = serializers.SerializerMethodField()

    class Meta:
        model = FotoProducto
        fields = ('producto', 'foto')

    def get_foto(self, obj):
        try:
            request = self.context.get('request')
            if obj.foto:
                foto_url = obj.foto.url
                return request.build_absolute_uri(foto_url)
            else:
                return None
        except FotoProducto.DoesNotExist:
            return None


class ProductoDetalleSerializer(serializers.ModelSerializer):
    categorias = serializers.PrimaryKeyRelatedField(many=True, queryset=Categoria.objects.all())
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    fotos = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'descripcion', 'marca', 'modelo', 'precio', 'categorias', 'created', 'edited', 'actived', 'fotos')
    def get_fotos(self, obj):
        try:
            fotos_productos = FotoProducto.objects.filter(producto=obj.id)
            if fotos_productos.exists():
                request = self.context.get('request')
                fotos_urls = [request.build_absolute_uri(foto.foto.url) for foto in fotos_productos]
                return fotos_urls   
            else:
                return None
        except FotoProducto.DoesNotExist:
            return None
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

class BodegaSerializer(serializers.ModelSerializer):
    ciudad_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Bodega
        fields = ('id', 'nombre',  'direccion', 'numeracion','ciudad','ciudad_nombre')
    def get_ciudad_nombre(self, obj):
        try:
            ciudad_obj = Ciudad.objects.get(id=obj.ciudad.id)
            return ciudad_obj.nombre
        except Ciudad.DoesNotExist:
            return None

class SucursalSerializer(serializers.ModelSerializer):
    ciudad_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Sucursal
        fields = ('id', 'nombre',  'direccion', 'numeracion','ciudad','ciudad_nombre')
    def get_ciudad_nombre(self, obj):
        try:
            ciudad_obj = Ciudad.objects.get(id=obj.ciudad.id)
            return ciudad_obj.nombre
        except Ciudad.DoesNotExist:
            return None

class MovimientoBodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoBodega
        fields = '__all__'



class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'
        
class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class FormaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPago
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    ciudad_nombre = serializers.SerializerMethodField()
    region_nombre = serializers.SerializerMethodField()
    ciudad = Ciudad()
    class Meta:
        model = Direccion
        fields = ('id', 
                  'cliente',  
                  'calle', 
                  'numero',
                  'ciudad',
                  'ciudad_nombre', 
                  'region_nombre',

                  )
    def get_ciudad_nombre(self, obj):
        try:
            ciudad_obj = Ciudad.objects.get(id=obj.ciudad.id)
            return ciudad_obj.nombre
        except Ciudad.DoesNotExist:
            return None
    def get_region_nombre(self, obj):
        try:
            ciudad_obj = Ciudad.objects.get(id=obj.ciudad.id)
            region_nombre = Region.objects.get(id=ciudad_obj.region.id)
            return region_nombre.nombre
        except Region.DoesNotExist:
            return None

class AtributoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atributo
        fields = '__all__'

class ValorAtributoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValorAtributo
        fields = '__all__'

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = '__all__'

class TipoProductoAtributoSerializer(serializers.ModelSerializer):
    atributo_nombre = serializers.CharField(source='atributo.nombre', read_only=True)
    atributo_valor = serializers.CharField(source='valorAtributo.valor', read_only=True)

    class Meta:
        model = TipoProductoAtributo
        fields = ['atributo_nombre', 'atributo_valor', 'producto', 'created', 'edited']

    def get_atributo_valor(self, obj):
        if obj.atributo and obj.valorAtributo:
            return f"{obj.atributo.nombre}: {obj.valorAtributo.valor}"
        return None


class CarritoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='producto.nombre', read_only=True)
    precio = serializers.IntegerField(source='producto.precio', read_only=True)
    descripcion = serializers.CharField(source='producto.descripcion', read_only=True)
    marca = serializers.CharField(source='producto.marca.nombre', read_only=True)


    

    class Meta:
        model = Carrito
        fields = ['id', 'cantidad', 'created', 'edited', 'producto', 'cliente', 'nombre', 'precio','marca','descripcion']




