from django.urls import path
from . import views

urlpatterns = [
    #Url inicio
    path('',views.home),
    #Url Raza 1
    path('listaRaza/',views.listaRaza),
    path('guardarRaza/',views.guardarRaza),
    path('eliminarRaza/<id>',views.eliminarRaza),
    path('editarRaza/<id>',views.editarRaza),
    path('actualizarRaza/',views.actualizarRaza),
    #Url Pais 2
    path('listaPais/',views.listaPais),
    path('guardarPais/',views.guardarPais),
    path('eliminarPais/<id>'    ,views.eliminarPais),
    path('editarPais/<id>',views.editarPais),
    path('actualizarPais/',views.actualizarPais),
    #Url EstadoCivil 3
    path('listaEstadoCivil/',views.listaEstadoCivil),
    path('guardarEstadoCivil/',views.guardarEstadoCivil),
    path('eliminarEstadoCivil/<id>',views.eliminarEstadoCivil),
    path('editarEstadoCivil/<id>',views.editarEstadoCivil),
    path('actualizarEstadoCivil/',views.actualizarEstadoCivil),
    #Url TipoAtencion 4
    path('listaTipoAtencion/',views.listaTipoAtencion),
    path('guardarTipoAtencion/',views.guardarTipoAtencion),
    path('eliminarTipoAtencion/<id>',views.eliminarTipoAtencion),
    path('editarTipoAtencion/<id>',views.editarTipoAtencion),
    path('actualizarTipoAtencion/',views.actualizarTipoAtencion),
    #Url Medicamento 5
    path('listaMedicamento/',views.listaMedicamento),
    path('guardarMedicamento/',views.guardarMedicamento),
    path('eliminarMedicamento/<id>',views.eliminarMedicamento),
    path('editarMedicamento/<id>',views.editarMedicamento),
    path('actualizarMedicamento/',views.actualizarMedicamento),
    #Url Propietario 6
    path('listaPropietario/',views.listaPropietario),
    path('guardarPropietario/',views.guardarPropietario),
    path('eliminarPropietario/<id>',views.eliminarPropietario),
    path('editarPropietario/<id>',views.editarPropietario),
    path('actualizarPropietario/',views.actualizarPropietario),
    # Url Mascota 7
    path('listaMascota/',views.listaMascota),
    path('guardarMascota/',views.guardarMascota),
    path('eliminarMascota/<id>',views.eliminarMascota),
    path('editarMascota/<id>',views.editarMascota),
    path('actualizarMascota/',views.actualizarMascota),
    # Url Atencion 8
    path('listaAtencion/',views.listaAtencion),
    path('guardarAtencion/',views.guardarAtencion),
    path('eliminarAtencion/<id>',views.eliminarAtencion),
    path('editarAtencion/<id>',views.editarAtencion),
    path('actualizarAtencion/',views.actualizarAtencion),
    # Url Receta 9
    path('listaReceta/',views.listaReceta),
    path('guardarReceta/',views.guardarReceta),
    path('eliminarReceta/<id>',views.eliminarReceta),
    path('editarReceta/<id>',views.editarReceta),
    path('actualizarReceta/',views.actualizarReceta),
    # Url Detalle 10
    path('listaDetalle/',views.listaDetalle),
    path('guardarDetalle/',views.guardarDetalle),
    path('eliminarDetalle/<id>',views.eliminarDetalle),
    path('editarDetalle/<id>',views.editarDetalle),
    path('actualizarDetalle/',views.actualizarDetalle),
    # Url PDFs11
]
