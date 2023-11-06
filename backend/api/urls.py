from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('backend/usuario/',   UsuarioList.as_view()),

    path('backend/region/',   RegionList.as_view()),
    path('backend/region/<int:id>/',   RegionDetail.as_view()),
    path('backend/ciudad/',   CiudadList.as_view()),
    path('backend/ciudad/<int:id>/',   CiudadDetail.as_view()),
    path('backend/genero/',   GeneroList.as_view()),
    path('backend/genero/<int:id>/',   GeneroDetail.as_view()),
    path('backend/marca/',   MarcaList.as_view()),
    path('backend/marca/<int:id>/',   MarcaDetail.as_view()),
    path('backend/cargo/',   CargoList.as_view()),
    path('backend/cargo/<int:id>/',   CargoDetail.as_view()),
    path('backend/categoria/',   CategoriaList.as_view()),
    path('backend/categoria/<int:id>/',   CategoriaDetail.as_view()),
    path('backend/atributo/',   AtributoList.as_view()),
    path('backend/atributo/<int:id>/',   AtributoDetail.as_view()),
    path('backend/valoratributo/',   ValorAtributoList.as_view()),
    path('backend/valoratributo/<int:id>/',   ValorAtributoDetail.as_view()),
    path('backend/direccion/',   DireccionList.as_view()),
    path('backend/direccion/<int:id>/',   DireccionDetail.as_view()),
    path('backend/clientedirecciones/<int:id>/',   DireccionListCliente.as_view()),
    path('backend/formapago/',   FormaPagoList.as_view()),
    path('backend/formapago/<int:id>/',   FormaPagoDetail.as_view()),
    path('backend/tarjeta/',   TarjetaList.as_view()),
    path('backend/tarjetascliente/<int:rut>/',   TarjetaListCliente.as_view()),
    path('backend/tarjeta/<int:id>/',   TarjetaDetail.as_view()),
    path('backend/ciudadregion/',   CiudadesRegiones.as_view()),
    path('backend/viewproductolist/',   ViewProductoList.as_view()),
    path('backend/viewproductolist/<int:ide>',   ViewProductoDetail.as_view()),
    path('backend/productoadd/',   ViewCategoriasMarcasAtributos.as_view()),
    path('backend/cliente/', ClienteList.as_view()),
    path('backend/cliente/<int:rut>', ClienteDetail.as_view()),
    path('backend/carrocliente/<int:rut>', CarroCliente.as_view()),
    path('backend/carroclientepost/', CarroClientePost.as_view()),
    path('backend/sucursal/',   SucursalList.as_view()),
    path('backend/sucursal/<int:id>/',   SucursalDetail.as_view()),
    path('backend/bodega/',   BodegaList.as_view()),
    path('backend/bodega/<int:id>/',   BodegaDetail.as_view()),
    path('backend/proveedor/',   ProveedorList.as_view()),
    path('backend/proveedor/<int:id>/',   ProveedorDetail.as_view()),
    path('backend/empleado/',   EmpleadoList.as_view()),
    path('backend/empleado/<int:id>/',  EmpleadoDetail.as_view()),
    path('backend/factura/',   FacturaList.as_view()),
    path('backend/factura/<int:id>/',  FacturaDetail.as_view()),
    path('backend/facturadetalle/<int:id>/',  FacturaDetalleDetail.as_view()),

    path('backend/boleta/',   BoletaList.as_view()),
    path('backend/boleta/<int:id>/',  BoletaDetail.as_view()),
    path('backend/boletadetalle/<int:id>/',  BoletaDetalleDetail.as_view()),


    
    path('backend/carritosucursal/',   CarritoSucursal.as_view()),
    path('backend/retirador/',   RetiradorCliente.as_view()),
    path('backend/generocargo/',   GeneroCargoList.as_view()),
    path('backend/empleadoedit/<int:id>/',   EmpleadoEdit.as_view()),

    path('backend/compraslist/<int:rut>/',   ComprasList.as_view()),



    path('backend/crearwebpay/',   CrearWebPay.as_view()),
    path('backend/errorpago/',   errorPago.as_view()),

    path('backend/cambiarclave/',   CambiarClaveUsuario.as_view()),
    path('backend/pedidos/',   PedidoList.as_view()),

    path('backend/proveedorlistaproducto/',   ProductoProveedorList.as_view()),
    path('backend/proveedordetalleproducto/<int:id>/',   ProductoProveedorDetail.as_view()),
    path('backend/bodegaproveedor/<int:id>/',   BodegaProveedor.as_view()),
    path('backend/productoproveedor/<int:id>/',   ProductoProveedor.as_view()),
    path('backend/productoproveedorlist/<int:ide>/',   ViewProductoProveedorList.as_view()),
    path('backend/abastecerproducto/',   AbastecerProducto.as_view()),

    path('backend/confirmarpedidosdetalle/<int:id>/',   ConfirmarEstadosDetail.as_view()),
    path('backend/confirmarpedidos/',   ConfirmarEstadosList.as_view()),

    path('backend/entradaproductoproveedor/',   EntradaProductoProveedorList.as_view()),
    path('backend/entradaproductoproveedor/<int:id>/',   EntradaProductoProveedorList.as_view()),

    path('backend/stockbodegas/',   StockBodegas.as_view()),
    path('backend/stockbodegasdetail/<int:id>',   StockBodegasDetail.as_view()),



    path('backend/stockproducto/',   StockProducto.as_view()),
    path('backend/stockproducto/<int:id>/',   StockProductoDetail.as_view()),


    path('backend/salidaproductodespacho/',   SalidaProductoDespacho.as_view()),
    path('backend/salidadetallepedidostock/<int:id>/',   SalidaDetallePedidoStock.as_view()),

    path('backend/crearsalidaproductodespacho/<int:rut>/',   CrearSalidaProductoDespacho.as_view()),

    path('backend/listaguiasdespacho/',   ListaGuiasDespachos.as_view()),
    path('backend/detalleguiadespacho/<int:id>/',   DetalleGuiaDespacho.as_view()),







####TESTTT# >>>>
    path('backend/bodegadistancia/',   BodegasDistancias.as_view()),





    path('backend/login/',   CustomTokenObtainPairView.as_view()),
    path('backend/log/',   LoginView.as_view()),

    path('backend/ciudadtest/',   ciudadtest.as_view()),







    path('backend/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('backend/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),







               

    path('categorias/', ListaCategorias, name='lista-categorias'),
    path('categorias/<int:id>/', DetalleCategoria, name='detalle-categoria'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)