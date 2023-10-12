from django.urls import path
from ProyectoApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('maquillajes/', maquillaje, name="Maquillajes"),
    path('accesorios/', accesorio, name="Accesorios"),
    path('usuarios/', usuario, name="Usuarios"),
    path("busquedaNombreMaquillaje/", busquedaNombreMaquillaje, name="buscarForm"),
    path("resultadosBusqueda/", resultadosBusqueda, name="resForm"),
    path("login/", inicioSesion, name="Login"),
    path("registro/", registro, name="Registro"),
    path("logout/", LogoutView.as_view(template_name="ProyectoApp/logout.html"), name="Logout"),
    path("editarUsuario/", editarUsuario, name="EditarUsuario"),
    path("agregarAvatar/", agregarAvatar, name="AgregarAvatar"),
    path("about/", about, name="About"),

    #Crud de Maquillaje con Clases
    path("maquillaje/list/", ListaMaquillaje.as_view() , name="ListaMaquillajes"),
    path("maquillaje/<int:pk>", DetalleMaquillaje.as_view() , name="DetalleMaquillaje"),
    path("maquillaje/crear/", CrearMaquillaje.as_view() , name="CrearMaquillaje"),
    path("maquillaje/editar/<int:pk>", EditarMaquillaje.as_view() , name="EditarMaquillaje"),
    path("maquillaje/eliminar/<int:pk>", EliminarMaquillaje.as_view() , name="EliminarMaquillaje"),

    #Crud de Accesorios con clases
    path("accesorio/list/", ListaAccesorios.as_view() , name="ListaAccesorios"),
    path("accesorio/<int:pk>", DetalleAccesorios.as_view() , name="DetalleAccesorio"),
    path("accesorio/crear/", CrearAccesorio.as_view() , name="CrearAccesorio"),
    path("accesorio/editar/<int:pk>", EditarAccesorio.as_view() , name="EditarAccesorio"),
    path("accesorio/eliminar/<int:pk>", EliminarAccesorio.as_view() , name="EliminarAccesorio"),

    #Crud de Cremas Faciales con clases
    path("cremasFaciales/list/", ListaCremasFaciales.as_view() , name="ListaCremasFaciales"),
    path("cremasFaciales/<int:pk>", DetalleCremaFacial.as_view() , name="DetalleCremaFacial"),
    path("cremasFaciales/crear/", CrearCremaFacial.as_view() , name="CrearCremaFacial"),
    path("cremasFaciales/editar/<int:pk>", EditarCremaFacial.as_view() , name="EditarCremaFacial"),
    path("cremasFaciales/eliminar/<int:pk>", EliminarCremaFacial.as_view() , name="EliminarCremaFacial"),

    #Crud de Cremas Faciales con clases
    path("cremasCorporales/list/", ListaCremasCorporales.as_view() , name="ListaCremasCorporales"),
    path("cremasCorporales/<int:pk>", DetalleCremaCorporal.as_view() , name="DetalleCremaCorporal"),
    path("cremasCorporales/crear/", CrearCremaCorporal.as_view() , name="CrearCremaCorporal"),
    path("cremasCorporales/editar/<int:pk>", EditarCremaCorporal.as_view() , name="EditarCremaCorporal"),
    path("cremasCorporales/eliminar/<int:pk>", EliminarCremaCorporal.as_view() , name="EliminarCremaCorporal"),

]


