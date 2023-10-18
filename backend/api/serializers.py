from rest_framework import serializers
from .models import *

class ViewClienteSerializer(serializers.ModelSerializer):
    ciudad_nombre = serializers.SerializerMethodField()
    genero_nombre = serializers.SerializerMethodField()
    nacimiento = serializers.SerializerMethodField()
    telefono = serializers.SerializerMethodField()

    class Meta:
        model = ViewCliente
        fields = ('rut', 'dv',  'nombre', 'appaterno', 'apmaterno', 'email','ciudad_nombre','genero_nombre','telefono','nacimiento','genero')
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

class ProductoDetalleSerializer(serializers.ModelSerializer):
    categorias = serializers.PrimaryKeyRelatedField(many=True, queryset=Categoria.objects.all())
    class Meta:
        model = Producto
        fields = '__all__'
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodega
        fields = '__all__'

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

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
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




