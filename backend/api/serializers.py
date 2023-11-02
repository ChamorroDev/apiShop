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


class FacturaSerializer(serializers.ModelSerializer):
    estadoPedido_nombre = serializers.SerializerMethodField()
    forma_pago_nombre = serializers.SerializerMethodField()
    tipoDespacho_nombre = serializers.SerializerMethodField()
    retiroPersona_info=serializers.SerializerMethodField()
    direccion_info = serializers.SerializerMethodField()

    def get_estadoPedido_nombre(self, obj):
        return obj.estadoPedido.nombre if obj.estadoPedido else None

    def get_forma_pago_nombre(self, obj):
        return obj.forma_pago.nombre if obj.forma_pago else None

    def get_tipoDespacho_nombre(self, obj):
        return obj.tipoDespacho.nombre if obj.tipoDespacho else None

    def get_retiroPersona_info(self, obj):
        if obj.retiroPersona:
            return f"{obj.retiroPersona.nombre} {obj.retiroPersona.apellido}"
        return None

    def get_direccion_info(self, obj):
        if obj.direccion:
            return f"{obj.direccion.calle} {obj.direccion.numero}, {obj.direccion.ciudad.nombre}, {obj.direccion.ciudad.region.nombre}"
        elif obj.sucursal:
            return f"{obj.sucursal.direccion} {obj.sucursal.numeracion}, {obj.sucursal.ciudad.nombre}, {obj.sucursal.ciudad.region.nombre}"
        return None
    
    class Meta:
        model = Factura
        fields = '__all__'

class BoletaSerializer(serializers.ModelSerializer):
    estadoPedido_nombre = serializers.SerializerMethodField()
    forma_pago_nombre = serializers.SerializerMethodField()
    tipoDespacho_nombre = serializers.SerializerMethodField()
    retiroPersona_info=serializers.SerializerMethodField()
    direccion_info = serializers.SerializerMethodField()

    def get_estadoPedido_nombre(self, obj):
        return obj.estadoPedido.nombre if obj.estadoPedido else None

    def get_forma_pago_nombre(self, obj):
        return obj.forma_pago.nombre if obj.forma_pago else None

    def get_tipoDespacho_nombre(self, obj):
        return obj.tipoDespacho.nombre if obj.tipoDespacho else None

    def get_retiroPersona_info(self, obj):
        if obj.retiroPersona:
            return f"{obj.retiroPersona.nombre} {obj.retiroPersona.apellido}"
        return None

    def get_direccion_info(self, obj):
        if obj.direccion:
            return f"{obj.direccion.calle} {obj.direccion.numero}, {obj.direccion.ciudad.nombre}, {obj.direccion.ciudad.region.nombre}"
        elif obj.sucursal:
            return f"{obj.sucursal.direccion} {obj.sucursal.numeracion}, {obj.sucursal.ciudad.nombre}, {obj.sucursal.ciudad.region.nombre}"
        return None
    class Meta:
        model = Boleta
        fields = '__all__'

class DetalleFacturaSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.SerializerMethodField()
    foto_producto = serializers.SerializerMethodField()
             
    def get_producto_nombre(self, obj):
            return obj.producto.nombre if obj.producto else None
    def get_foto_producto(self, obj):
        if obj.producto and obj.producto.fotos.exists():
            primera_foto = obj.producto.fotos.first()
            request = self.context.get('request')

            return request.build_absolute_uri(primera_foto.foto.url) if primera_foto else None
        return None
    class Meta:
        model = DetalleFactura
        fields = '__all__'

class DetalleBoletaSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.SerializerMethodField()
    foto_producto = serializers.SerializerMethodField()
             
    def get_producto_nombre(self, obj):
            return obj.producto.nombre if obj.producto else None
    def get_foto_producto(self, obj):
        if obj.producto and obj.producto.fotos.exists():
            primera_foto = obj.producto.fotos.first()
            request = self.context.get('request')

            return request.build_absolute_uri(primera_foto.foto.url) if primera_foto else None
        return None
    class Meta:
        model = DetalleBoleta
        fields = '__all__'

class ProductoProveedorTablaSerializer(serializers.ModelSerializer):
    proveedor_nombre = serializers.SerializerMethodField()

    class Meta:
        model = ProductoProveedor
        fields = ('precio','proveedor_nombre')
    def get_proveedor_nombre(self, obj):
            return obj.proveedor.nombre if obj.proveedor else None

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

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
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

class ProductoProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre', 'marca', 'modelo', 'precio')

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
    region_nombre = serializers.SerializerMethodField()


    class Meta:
        model = Bodega
        fields = ('id', 'nombre',  'direccion', 'numeracion','ciudad','ciudad_nombre','region_nombre')
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



class ComprasProveedorSerializer(serializers.ModelSerializer):
    estado_nombre = serializers.CharField(source='estado.nombre', read_only=True)
    usuario_nombre = serializers.CharField(source='usuario.usuario', read_only=True)
    proveedor_nombre = serializers.CharField(source='proveedor.nombre', read_only=True)
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    bodega_info = BodegaSerializer(source='bodega', read_only=True)


    class Meta:
        model = ComprasProveedor
        fields = ['id','estado_nombre','producto_nombre', 'precio','created','usuario_nombre','proveedor_nombre','cantidad','bodega_info','obs','cantidad_recibida']


class ProductoCantidadSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    foto_producto = serializers.SerializerMethodField()

    def get_foto_producto(self, obj):
        if obj.producto and obj.producto.fotos.exists():
            primera_foto = obj.producto.fotos.first()
            request = self.context.get('request')

            return request.build_absolute_uri(primera_foto.foto.url) if primera_foto else None
        return None

    class Meta:
        model = ComprasProveedor
        fields = ['producto_nombre','cantidad','foto_producto']