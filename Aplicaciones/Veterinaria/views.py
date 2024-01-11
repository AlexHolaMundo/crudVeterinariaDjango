from django.shortcuts import render, redirect
from .models import Raza,Pais,EstadoCivil,TipoAtencion,Medicamento, Propietario, Mascota, Atencion, Receta, Detalle
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def listaRaza(request):
    razaBdd=Raza.objects.all()
    return render(request,'listaRaza.html',{'razas':razaBdd})

def guardarRaza(request):
    nombre_wt=request.POST["nombre_wt"]
    descripcion_wt=request.POST["descripcion_wt"]
    origen_wt=request.POST["origen_wt"]
    esperanzaVida_wt=request.POST["esperanzaVida_wt"]
    caracteristica_wt=request.POST["caracteristica_wt"]

    nuevaRaza=Raza.objects.create(
        nombre_wt=nombre_wt,
        descripcion_wt=descripcion_wt,
        origen_wt=origen_wt,
        esperanzaVida_wt=esperanzaVida_wt,
        caracteristica_wt=caracteristica_wt
        )
    messages.success(request,"Raza Guardada Correctamente")
    return redirect('/listaRaza')

def eliminarRaza(request,id):
    razaEliminar=Raza.objects.get(idRaza_wt=id)
    razaEliminar.delete()
    messages.success(request,"Raza Eliminada Correctamente")
    return redirect(listaRaza)

def editarRaza(request,id):
    razaEditar=Raza.objects.get(idRaza_wt=id)
    return render(request,'editarRaza.html',{'raza':razaEditar})

def actualizarRaza(request):
    id=request.POST["idRaza_wt"]
    nombre_wt=request.POST["nombre_wt"]
    descripcion_wt=request.POST["descripcion_wt"]
    origen_wt=request.POST["origen_wt"]
    esperanzaVida_wt=request.POST["esperanzaVida_wt"]
    caracteristica_wt=request.POST["caracteristica_wt"]

    razaActualizar=Raza(
        idRaza_wt=id,
        nombre_wt=nombre_wt,
        descripcion_wt=descripcion_wt,
        origen_wt=origen_wt,
        esperanzaVida_wt=esperanzaVida_wt,
        caracteristica_wt=caracteristica_wt
        )
    razaActualizar.save()
    messages.success(request,"Raza Actualizada Correctamente")
    return redirect(listaRaza)

def listaPais(request):
    paisBdd=Pais.objects.all()
    return render(request,'listaPais.html',{'paises':paisBdd})

def guardarPais(request):
    nombre_wt=request.POST["nombre_wt"]
    capital_wt=request.POST["capital_wt"]
    poblacion_wt=request.POST["poblacion_wt"]
    idioma_wt=request.POST["idioma_wt"]
    moneda_wt=request.POST["moneda_wt"]

    imgBandera_wt=request.FILES.get("imgBandera_wt")

    nuevoPais=Pais.objects.create(
        nombre_wt=nombre_wt,
        capital_wt=capital_wt,
        poblacion_wt=poblacion_wt,
        idioma_wt=idioma_wt,
        moneda_wt=moneda_wt,
        imgBandera_wt=imgBandera_wt
        )
    messages.success(request,"Pais Guardado Correctamente")
    return redirect('/listaPais')

def eliminarPais(request,id):
    paisEliminar=Pais.objects.get(idPais_wt=id)
    paisEliminar.delete()
    messages.success(request,"Pais Eliminado Correctamente")
    return redirect(listaPais)

def editarPais(request,id):
    paisEditar=Pais.objects.get(idPais_wt=id)
    return render(request,'editarPais.html',{'pais':paisEditar})

def actualizarPais(request):
    id=request.POST["idPais_wt"]
    nombre_wt=request.POST["nombre_wt"]
    capital_wt=request.POST["capital_wt"]
    poblacion_wt=request.POST["poblacion_wt"]
    idioma_wt=request.POST["idioma_wt"]
    moneda_wt=request.POST["moneda_wt"]
    imgBandera_wt=request.FILES.get("imgBandera_wt")

    paisActualizar=Pais(
        idPais_wt=id,
        nombre_wt=nombre_wt,
        capital_wt=capital_wt,
        poblacion_wt=poblacion_wt,
        idioma_wt=idioma_wt,
        moneda_wt=moneda_wt,
        imgBandera_wt=imgBandera_wt
        )
    paisActualizar.save()
    messages.success(request,"Pais Actualizado Correctamente")
    return redirect(listaPais)

def listaEstadoCivil(request):
    estadoCivilBdd=EstadoCivil.objects.all()
    return render(request,'listaEstadoCivil.html',{'estadoCivil':estadoCivilBdd})

def guardarEstadoCivil(request):
    descripcion_wt=request.POST["descripcion_wt"]
    edad_wt=request.POST["edad_wt"]
    numeroHijos_wt=request.POST["numeroHijos_wt"]
    tiempoEstado_wt=request.POST["tiempoEstado_wt"]
    actividad_wt=request.POST["actividad_wt"]

    nuevoEstadoCivil=EstadoCivil.objects.create(
        descripcion_wt=descripcion_wt,
        edad_wt=edad_wt,
        numeroHijos_wt=numeroHijos_wt,
        tiempoEstado_wt=tiempoEstado_wt,
        actividad_wt=actividad_wt
        )
    messages.success(request,"Estado Civil Guardado Correctamente")
    return redirect(listaEstadoCivil)

def eliminarEstadoCivil(request,id):
    estadoCivilEliminar=EstadoCivil.objects.get(idEstadoCivil_wt=id)
    estadoCivilEliminar.delete()
    messages.success(request,"Estado Civil Eliminado Correctamente")
    return redirect(listaEstadoCivil)

def editarEstadoCivil(request,id):
    estadoCivilEditar=EstadoCivil.objects.get(idEstadoCivil_wt=id)
    return render(request,'editarEstadoCivil.html',{'estadoCivil':estadoCivilEditar})

def actualizarEstadoCivil(request):
    id=request.POST["idEstadoCivil_wt"]
    descripcion_wt=request.POST["descripcion_wt"]
    edad_wt=request.POST["edad_wt"]
    numeroHijos_wt=request.POST["numeroHijos_wt"]
    tiempoEstado_wt=request.POST["tiempoEstado_wt"]
    actividad_wt=request.POST["actividad_wt"]

    estadoCivilActualizar=EstadoCivil(
        idEstadoCivil_wt=id,
        descripcion_wt=descripcion_wt,
        edad_wt=edad_wt,
        numeroHijos_wt=numeroHijos_wt,
        tiempoEstado_wt=tiempoEstado_wt,
        actividad_wt=actividad_wt
        )
    estadoCivilActualizar.save()
    messages.success(request,"Estado Civil Actualizado Correctamente")
    return redirect('/listaEstadoCivil')

def listaTipoAtencion(request):
    tipoAtencionBdd=TipoAtencion.objects.all()
    return render(request,'listaTipoAtencion.html',{'tipoAtencion':tipoAtencionBdd})

def guardarTipoAtencion(request):
    costo_wt=request.POST["costo_wt"]
    especialidades_wt=request.POST["especialidades_wt"]
    disponibilidad_wt=request.POST["disponibilidad_wt"]
    tiempoEspera_wt=request.POST["tiempoEspera_wt"]
    comentarios_wt=request.POST["comentarios_wt"]

    nuevoTipoAtencion=TipoAtencion.objects.create(
        costo_wt=costo_wt,
        especialidades_wt=especialidades_wt,
        disponibilidad_wt=disponibilidad_wt,
        tiempoEspera_wt=tiempoEspera_wt,
        comentarios_wt=comentarios_wt
        )
    messages.success(request,"Tipo Atencion Guardado Correctamente")
    return redirect(listaTipoAtencion)

def eliminarTipoAtencion(request,id):
    tipoAtencionEliminar=TipoAtencion.objects.get(idTipoAtencion_wt=id)
    tipoAtencionEliminar.delete()
    messages.success(request,"Tipo Atencion Eliminado Correctamente")
    return redirect(listaTipoAtencion)

def editarTipoAtencion(request,id):
    tipoAtencionEditar=TipoAtencion.objects.get(idTipoAtencion_wt=id)
    return render(request,'editarTipoAtencion.html',{'tipoAtencion':tipoAtencionEditar})

def actualizarTipoAtencion(request):
    id=request.POST["idTipoAtencion_wt"]
    costo_wt=request.POST["costo_wt"]
    especialidades_wt=request.POST["especialidades_wt"]
    disponibilidad_wt=request.POST["disponibilidad_wt"]
    tiempoEspera_wt=request.POST["tiempoEspera_wt"]
    comentarios_wt=request.POST["comentarios_wt"]

    tipoAtencionActualizar=TipoAtencion(
        idTipoAtencion_wt=id,
        costo_wt=costo_wt,
        especialidades_wt=especialidades_wt,
        disponibilidad_wt=disponibilidad_wt,
        tiempoEspera_wt=tiempoEspera_wt,
        comentarios_wt=comentarios_wt
        )
    tipoAtencionActualizar.save()
    messages.success(request,"Tipo Atencion Actualizado Correctamente")
    return redirect(listaTipoAtencion)

def listaMedicamento(request):
    medicamentoBdd=Medicamento.objects.all()
    return render(request,'listaMedicamento.html',{'medicamentos':medicamentoBdd})

def guardarMedicamento(request):
    nombre_wt=request.POST["nombre_wt"]
    descripcion_wt=request.POST["descripcion_wt"]
    efectosSecundarios_wt=request.POST["efectosSecundarios_wt"]
    precio_wt=request.POST["precio_wt"]
    instrucciones_wt=request.POST["instrucciones_wt"]

    imgMedicamento_wt=request.FILES.get("imgMedicamento_wt")

    nuevoMedicamento=Medicamento.objects.create(
        nombre_wt=nombre_wt,
        descripcion_wt=descripcion_wt,
        efectosSecundarios_wt=efectosSecundarios_wt,
        precio_wt=precio_wt,
        instrucciones_wt=instrucciones_wt,
        imgMedicamento_wt=imgMedicamento_wt
        )
    messages.success(request,"Medicamento Guardado Correctamente")
    return redirect(listaMedicamento)

def eliminarMedicamento(request,id):
    medicamentoEliminar=Medicamento.objects.get(idMedicamento_wt=id)
    medicamentoEliminar.delete()
    messages.success(request,"Medicamento Eliminado Correctamente")
    return redirect(listaMedicamento)

def editarMedicamento(request,id):
    medicamentoEditar=Medicamento.objects.get(idMedicamento_wt=id)
    return render(request,'editarMedicamento.html',{'medicamento':medicamentoEditar})

def actualizarMedicamento(request):
    id=request.POST["idMedicamento_wt"]
    nombre_wt=request.POST["nombre_wt"]
    descripcion_wt=request.POST["descripcion_wt"]
    efectosSecundarios_wt=request.POST["efectosSecundarios_wt"]
    precio_wt=request.POST["precio_wt"]
    instrucciones_wt=request.POST["instrucciones_wt"]
    imgMedicamento_wt=request.FILES.get("imgMedicamento_wt")

    medicamentoActualizar=Medicamento(
        idMedicamento_wt=id,
        nombre_wt=nombre_wt,
        descripcion_wt=descripcion_wt,
        efectosSecundarios_wt=efectosSecundarios_wt,
        precio_wt=precio_wt,
        instrucciones_wt=instrucciones_wt,
        imgMedicamento_wt=imgMedicamento_wt
        )
    medicamentoActualizar.save()

    messages.success(request,"Medicamento Actualizado Correctamente")
    return redirect(listaMedicamento)

def listaPropietario(request):
    propietarioBdd=Propietario.objects.all()
    paisBdd=Pais.objects.all()
    estadoCivilBdd=EstadoCivil.objects.all()
    return render(request,'listaPropietario.html',{'propietarios':propietarioBdd,'paises':paisBdd,'estadoCivil':estadoCivilBdd })

def guardarPropietario(request):
    pais_wt=request.POST["idPais_wt"]
    paisSeleccionado_wt=Pais.objects.get(idPais_wt=pais_wt)

    estadoCivil_wt=request.POST["idEstadoCivil_wt"]
    estadoCivilSeleccionado_wt=EstadoCivil.objects.get(idEstadoCivil_wt=estadoCivil_wt)

    nombre_wt=request.POST["nombre_wt"]
    apellido_wt=request.POST["apellido_wt"]
    direccion_wt=request.POST["direccion_wt"]
    telefono_wt=request.POST["telefono_wt"]
    correo_wt=request.POST["correo_wt"]

    pdfCedula_wt=request.FILES.get("pdfCedula_wt")

    nuevoPropietario = Propietario.objects.create(
        nombre_wt=nombre_wt,
        apellido_wt=apellido_wt,
        direccion_wt=direccion_wt,
        telefono_wt=telefono_wt,
        correo_wt=correo_wt,
        pais_wt=paisSeleccionado_wt,
        estadoCivil_wt=estadoCivilSeleccionado_wt,
        pdfCedula_wt=pdfCedula_wt
    )
    messages.success(request,"Propietario Guardado Correctamente")
    return redirect(listaPropietario)

def eliminarPropietario(request,id):
    propietarioEliminar=Propietario.objects.get(idPropietario_wt=id)
    propietarioEliminar.delete()
    messages.success(request,"Propietario Eliminado Correctamente")
    return redirect(listaPropietario)

def editarPropietario(request,id):
    propietarioEditar=Propietario.objects.get(idPropietario_wt=id)
    paisBdd=Pais.objects.all()
    estadoCivilBdd=EstadoCivil.objects.all()
    return render(request,'editarPropietario.html',{'propietario':propietarioEditar, 'paises':paisBdd, 'estadoCivil':estadoCivilBdd})

def actualizarPropietario(request):
    id=request.POST["idPropietario_wt"]

    idPais_wt=request.POST["idPais_wt"]
    paisSeleccionado_wt=Pais.objects.get(idPais_wt=idPais_wt)

    idEstadoCivil_wt=request.POST["idEstadoCivil_wt"]
    estadoCivilSeleccionado_wt=EstadoCivil.objects.get(idEstadoCivil_wt=idEstadoCivil_wt)

    nombre_wt=request.POST["nombre_wt"]
    apellido_wt=request.POST["apellido_wt"]
    direccion_wt=request.POST["direccion_wt"]
    telefono_wt=request.POST["telefono_wt"]
    correo_wt=request.POST["correo_wt"]
    pdfCedula_wt=request.FILES.get("pdfCedula_wt")

    propietarioActualizar=Propietario(
        idPropietario_wt=id,
        nombre_wt=nombre_wt,
        apellido_wt=apellido_wt,
        direccion_wt=direccion_wt,
        telefono_wt=telefono_wt,
        correo_wt=correo_wt,
        pais_wt=paisSeleccionado_wt,
        estadoCivil_wt=estadoCivilSeleccionado_wt,
        pdfCedula_wt=pdfCedula_wt
    )
    propietarioActualizar.save()
    messages.success(request,"Propietario Actualizado Correctamente")
    return redirect(listaPropietario)

def listaMascota(request):
    mascotaBdd=Mascota.objects.all()
    propietarioBdd=Propietario.objects.all()
    razaBdd=Raza.objects.all()
    return render(request,'listaMascota.html',{'mascotas':mascotaBdd,'propietarios':propietarioBdd,'razas':razaBdd})

def guardarMascota(request):
    propietario_wt=request.POST["idPropietario_wt"]
    propietarioSeleccionado_wt=Propietario.objects.get(idPropietario_wt=propietario_wt)

    raza_wt=request.POST["idRaza_wt"]
    razaSeleccionado_wt=Raza.objects.get(idRaza_wt=raza_wt)

    nombre_wt=request.POST["nombre_wt"]
    especie_wt=request.POST["especie_wt"]
    edad_wt=request.POST["edad_wt"]
    peso_wt=request.POST["peso_wt"]

    imgMascota_wt=request.FILES.get("imgMascota_wt")

    nuevaMascota=Mascota.objects.create(
        nombre_wt=nombre_wt,
        especie_wt=especie_wt,
        edad_wt=edad_wt,
        peso_wt=peso_wt,
        raza_wt=razaSeleccionado_wt,
        propietario_wt=propietarioSeleccionado_wt,
        imgMascota_wt=imgMascota_wt
    )
    messages.success(request,"Mascota Guardada Correctamente")
    return redirect(listaMascota)

def eliminarMascota(request,id):
    mascotaEliminar=Mascota.objects.get(idMascota_wt=id)
    mascotaEliminar.delete()
    messages.success(request,"Mascota Eliminada Correctamente")
    return redirect(listaMascota)

def editarMascota(request,id):
    mascotaEditar=Mascota.objects.get(idMascota_wt=id)
    propietarioBdd=Propietario.objects.all()
    razaBdd=Raza.objects.all()
    return render(request,'editarMascota.html',{'mascota':mascotaEditar, 'propietarios':propietarioBdd, 'razas':razaBdd})

def actualizarMascota(request):
    id=request.POST["idMascota_wt"]

    idPropietario_wt=request.POST["idPropietario_wt"]
    propietarioSeleccionado_wt=Propietario.objects.get(idPropietario_wt=idPropietario_wt)

    idRaza_wt=request.POST["idRaza_wt"]
    razaSeleccionado_wt=Raza.objects.get(idRaza_wt=idRaza_wt)

    nombre_wt=request.POST["nombre_wt"]
    especie_wt=request.POST["especie_wt"]
    edad_wt=request.POST["edad_wt"]
    peso_wt=request.POST["peso_wt"]
    imgMascota_wt=request.FILES.get("imgMascota_wt")

    mascotaActualizar=Mascota(
        idMascota_wt=id,
        nombre_wt=nombre_wt,
        especie_wt=especie_wt,
        edad_wt=edad_wt,
        peso_wt=peso_wt,
        raza_wt=razaSeleccionado_wt,
        propietario_wt=propietarioSeleccionado_wt,
        imgMascota_wt=imgMascota_wt
    )
    mascotaActualizar.save()
    messages.success(request,"Mascota Actualizada Correctamente")
    return redirect(listaMascota)

def listaAtencion(request):
    atencionBdd=Atencion.objects.all()
    tipoAtencionBdd=TipoAtencion.objects.all()
    mascotaBdd=Mascota.objects.all()
    return render(request,'listaAtencion.html',{'atenciones':atencionBdd,'tipoAt            enciones':tipoAtencionBdd,'mascotas':mascotaBdd})

def guardarAtencion(request):
    tipoAtencion_wt=request.POST["idTipoAtencion_wt"]
    tipoAtencionSeleccionado_wt=TipoAtencion.objects.get(idTipoAtencion_wt=tipoAtencion_wt)

    mascota_wt=request.POST["idMascota_wt"]
    mascotaSeleccionado_wt=Mascota.objects.get(idMascota_wt=mascota_wt)

    fecha_wt=request.POST["fecha_wt"]
    descripcion_wt=request.POST["descripcion_wt"]
    costo_wt=request.POST["costo_wt"]
    observaciones_wt=request.POST["observaciones_wt"]

    nuevaAtencion=Atencion.objects.create(
        fecha_wt=fecha_wt,
        descripcion_wt=descripcion_wt,
        costo_wt=costo_wt,
        observaciones_wt=observaciones_wt,
        tipoAtencion_wt=tipoAtencionSeleccionado_wt,
        mascota_wt=mascotaSeleccionado_wt
        )
    messages.success(request,"Atencion Guardada Correctamente")
    return redirect(listaAtencion)

def eliminarAtencion(request,id):
    atencionEliminar=Atencion.objects.get(idAtencion_wt=id)
    atencionEliminar.delete()
    messages.success(request,"Atencion Eliminada Correctamente")
    return redirect(listaAtencion)

def editarAtencion(request,id):
    atencionEditar=Atencion.objects.get(idAtencion_wt=id)
    tipoAtencionBdd=TipoAtencion.objects.all()
    mascotaBdd=Mascota.objects.all()
    return render(request,'editarAtencion.html',{'atencion':atencionEditar, 'tipoAtenciones':tipoAtencionBdd, 'mascotas':mascotaBdd})

def actualizarAtencion(request):
    id=request.POST["idAtencion_wt"]
    fecha_wt=request.POST["fecha_wt"]
    descripcion_wt=request.POST["descripcion_wt"]
    costo_wt=request.POST["costo_wt"]
    observaciones_wt=request.POST["observaciones_wt"]

    atencionActualizar=Atencion(
        idAtencion_wt=id,
        fecha_wt=fecha_wt,
        descripcion_wt=descripcion_wt,
        costo_wt=costo_wt,
        observaciones_wt=observaciones_wt
        )

    atencionActualizar.save()
    messages.success(request,"Atencion Actualizada Correctamente")
    return redirect(listaAtencion)

def listaReceta(request):
    recetaBdd=Receta.objects.all()
    atencionBdd=Atencion.objects.all()
    return render(request,'listaReceta.html',{'recetas':recetaBdd,'atenciones':atencionBdd})

def guardarReceta(request):
    atencion_wt=request.POST["idAtencion_wt"]
    atencionSeleccionado_wt=Atencion.objects.get(idAtencion_wt=atencion_wt)

    fechaEmision_wt=request.POST["fechaEmision_wt"]
    dosis_wt=request.POST["dosis_wt"]
    instrucciones_wt=request.POST["instrucciones_wt"]
    duracion_wt=request.POST["duracion_wt"]

    nuevaReceta=Receta.objects.create(
        fechaEmision_wt=fechaEmision_wt,
        dosis_wt=dosis_wt,
        instrucciones_wt=instrucciones_wt,
        duracion_wt=duracion_wt,
        atencion_wt=atencionSeleccionado_wt
        )
    messages.success(request,"Receta Guardada Correctamente")
    return redirect(listaReceta)

def eliminarReceta(request,id):
    recetaEliminar=Receta.objects.get(idReceta_wt=id)
    recetaEliminar.delete()
    messages.success(request,"Receta Eliminada Correctamente")
    return redirect(listaReceta)

def editarReceta(request,id):
    recetaEditar=Receta.objects.get(idReceta_wt=id)
    atencionBdd=Atencion.objects.all()
    return render(request,'editarReceta.html',{'receta':recetaEditar, 'atenciones':atencionBdd})

def actualizarReceta(request):
    id=request.POST["idReceta_wt"]

    idAtencion_wt=request.POST["idAtencion_wt"]
    atencionSeleccionado_wt=Atencion.objects.get(idAtencion_wt=idAtencion_wt)

    fechaEmision_wt=request.POST["fechaEmision_wt"]
    dosis_wt=request.POST["dosis_wt"]
    instrucciones_wt=request.POST["instrucciones_wt"]
    duracion_wt=request.POST["duracion_wt"]

    recetaActualizar=Receta(
        idReceta_wt=id,
        fechaEmision_wt=fechaEmision_wt,
        dosis_wt=dosis_wt,
        instrucciones_wt=instrucciones_wt,
        duracion_wt=duracion_wt,
        atencion_wt=atencionSeleccionado_wt
        )
    recetaActualizar.save()
    messages.success(request,"Receta Actualizada Correctamente")
    return redirect(listaReceta)

def listaDetalle(request):
    detalleBdd=Detalle.objects.all()
    recetaBdd=Receta.objects.all()
    medicamentoBdd=Medicamento.objects.all()
    return render(request,'listaDetalle.html',{'detalles':detalleBdd,'recetas':recetaBdd,'medicamentos':medicamentoBdd})

def guardarDetalle(request):
    receta_wt=request.POST["idReceta_wt"]
    recetaSeleccionado_wt=Receta.objects.get(idReceta_wt=receta_wt)

    medicamento_wt=request.POST["idMedicamento_wt"]
    medicamentoSeleccionado_wt=Medicamento.objects.get(idMedicamento_wt=medicamento_wt)

    precioUnitario_wt=request.POST["precioUnitario_wt"]
    descuento_wt=request.POST["descuento_wt"]
    subtotal_wt=request.POST["subtotal_wt"]

    nuevoDetalle=Detalle.objects.create(
        precioUnitario_wt=precioUnitario_wt,
        descuento_wt=descuento_wt,
        subtotal_wt=subtotal_wt,
        receta_wt=recetaSeleccionado_wt,
        medicamento_wt=medicamentoSeleccionado_wt
        )
    messages.success(request,"Detalle Guardado Correctamente")
    return redirect(listaDetalle)

def eliminarDetalle(request,id):
    detalleEliminar=Detalle.objects.get(idDetalle_wt=id)
    detalleEliminar.delete()
    messages.success(request,"Detalle Eliminado Correctamente")
    return redirect(listaDetalle)

def editarDetalle(request,id):
    detalleEditar=Detalle.objects.get(idDetalle_wt=id)
    recetaBdd=Receta.objects.all()
    medicamentoBdd=Medicamento.objects.all()
    return render(request,'editarDetalle.html',{'detalle':detalleEditar, 'recetas':recetaBdd, 'medicamentos':medicamentoBdd})

def actualizarDetalle(request):
    id=request.POST["idDetalle_wt"]
    precioUnitario_wt=request.POST["precioUnitario_wt"]
    descuento_wt=request.POST["descuento_wt"]
    subtotal_wt=request.POST["subtotal_wt"]

    detalleActualizar=Detalle(
        idDetalle_wt=id,
        precioUnitario_wt=precioUnitario_wt,
        descuento_wt=descuento_wt,
        subtotal_wt=subtotal_wt
        )

    detalleActualizar.save()
    messages.success(request,"Detalle Actualizado Correctamente")
    return redirect(listaDetalle)
