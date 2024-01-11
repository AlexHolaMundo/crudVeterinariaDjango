from django.db import models

# Create your models here.
class Raza(models.Model):
    idRaza_wt=models.AutoField(primary_key=True)
    nombre_wt=models.CharField(max_length=50)
    descripcion_wt=models.CharField(max_length=100)
    origen_wt=models.CharField(max_length=50)
    esperanzaVida_wt=models.IntegerField(default=0)
    caracteristica_wt=models.TextField(max_length=50)
    def __str__(self):
        fila="{0} => {1} => {2} => {3} => {4} => {5}"
        return fila.format(self.idRaza_wt,self.nombre_wt,self.descripcion_wt,self.origen_wt,self.esperanzaVida_wt,self.caracteristica_wt)

class Pais (models.Model):
    idPais_wt=models.AutoField(primary_key=True)
    nombre_wt=models.CharField(max_length=50)
    capital_wt=models.CharField(max_length=50)
    poblacion_wt=models.IntegerField()
    idioma_wt=models.CharField(max_length=50)
    moneda_wt=models.CharField(max_length=50)
    imgBandera_wt=models.FileField(upload_to='banderas', null=True, blank=True)
    def __str__(self):
        fila="{0} => {1} => {2} => {3} => {4} => {5}"
        return fila.format(self.idPais_wt,self.nombre_wt,self.capital_wt,self.poblacion_wt,self.idioma_wt,self.moneda_wt)

class EstadoCivil(models.Model):
    idEstadoCivil_wt=models.AutoField(primary_key=True)
    descripcion_wt=models.CharField(max_length=100)
    edad_wt=models.IntegerField()
    numeroHijos_wt=models.IntegerField()
    tiempoEstado_wt=models.IntegerField()
    actividad_wt=models.CharField(max_length=100)
    def __str__(self):
        fila="{0} => {1} => {2} => {3} => {4} => {5}"
        return fila.format(self.idEstadoCivil_wt,self.descripcion_wt,self.edad_wt,self.numeroHijos_wt,self.tiempoEstado_wt,self.actividad_wt)

class TipoAtencion(models.Model):
    idTipoAtencion_wt=models.AutoField(primary_key=True)
    costo_wt=models.IntegerField()
    especialidades_wt=models.CharField(max_length=100)
    disponibilidad_wt=models.CharField(max_length=100)
    tiempoEspera_wt=models.CharField(max_length=100)
    comentarios_wt=models.CharField(max_length=100)
    def __str__(self):
        fila="{0} => {1} => {2} => {3} => {4} => {5}"
        return fila.format(self.idTipoAtencion_wt,self.costo_wt,self.especialidades_wt,self.disponibilidad_wt,self.tiempoEspera_wt,self.comentarios_wt)

class Medicamento(models.Model):
    idMedicamento_wt=models.AutoField(primary_key=True)
    nombre_wt=models.CharField(max_length=100)
    descripcion_wt=models.CharField(max_length=100)
    efectosSecundarios_wt=models.CharField(max_length=100)
    precio_wt=models.IntegerField()
    instrucciones_wt=models.CharField(max_length=100)
    imgMedicamento_wt=models.FileField(upload_to='medicamentos', null=True, blank=True)
    def __str__(self):
        fila="{0} => {1} => {2} => {3} => {4} => {5}"
        return fila.format(self.idMedicamento_wt,self.nombre_wt,self.descripcion_wt,self.efectosSecundarios_wt,self.precio_wt,self.instrucciones_wt)

class Propietario(models.Model):
    idPropietario_wt=models.AutoField(primary_key=True)
    nombre_wt=models.CharField(max_length=100)
    apellido_wt=models.CharField(max_length=100)
    direccion_wt=models.CharField(max_length=100)
    telefono_wt=models.IntegerField()
    correo_wt=models.CharField(max_length=100)
    pais_wt=models.ForeignKey(Pais, null=True, blank=True, on_delete=models.CASCADE)
    estadoCivil_wt=models.ForeignKey(EstadoCivil,null=True, blank=True, on_delete=models.CASCADE)
    pdfCedula_wt=models.FileField(upload_to='cedulas', null=True, blank=True)
    def __str__(self) -> str:
        fila="{0} => {1} => {2} => {3} => {4} => {5} => {6} => {7}"
        return fila.format(self.idPropietario_wt,self.nombre_wt,self.apellido_wt,self.direccion_wt,self.telefono_wt,self.correo_wt,self.pais_wt,self.estadoCivil_wt)

class Mascota(models.Model):
    idMascota_wt=models.AutoField(primary_key=True)
    nombre_wt=models.CharField(max_length=100)
    especie_wt=models.CharField(max_length=100)
    edad_wt=models.IntegerField()
    peso_wt=models.IntegerField()
    raza_wt=models.ForeignKey(Raza, null=True, blank=True, on_delete=models.CASCADE)
    propietario_wt=models.ForeignKey(Propietario, null=True, blank=True, on_delete=models.CASCADE)
    imgMascota_wt=models.FileField(upload_to='mascotas', null=True, blank=True)
    def __str__(self):
        fila="{0} => {1} => {2} => {3} => {4} => {5}"
        return fila.format(self.idMascota_wt,self.nombre_wt,self.especie_wt,self.edad_wt,self.peso_wt,self.raza_wt,self.propietario_wt)

class Atencion(models.Model):
    idAtencion_wt=models.AutoField(primary_key=True)
    fecha_wt=models.DateField()
    descripcion_wt=models.CharField(max_length=100)
    costo_wt=models.IntegerField()
    observaciones_wt=models.CharField(max_length=100)
    tipoAtencion_wt=models.ForeignKey(TipoAtencion, null=True, blank=True, on_delete=models.CASCADE)
    mascota_wt=models.ForeignKey(Mascota, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self) -> str:
        fila="{0} => {1} => {2} => {3} => {4} => {5} => {6}"
        return fila.format(self.idAtencion_wt,self.fecha_wt,self.descripcion_wt,self.costo_wt,self.observaciones_wt,self.tipoAtencion_wt,self.mascota_wt)

class Receta(models.Model):
    idReceta_wt=models.AutoField(primary_key=True)
    fechaEmision_wt=models.DateField()
    dosis_wt=models.CharField(max_length=100)
    instrucciones_wt=models.CharField(max_length=100)
    duracion_wt=models.CharField(max_length=100)
    atencion_wt=models.ForeignKey(Atencion, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self) -> str:
        fila="{0} => {1} => {2} => {3} => {4} => {5}"
        return fila.format(self.idreceta_wt,self.fechaEmision_wt,self.dosis_wt,self.instrucciones_wt,self.duracion_wt,self.atencion_wt)

class Detalle(models.Model):
    idDetalle_wt=models.AutoField(primary_key=True)
    precioUnitario_wt=models.IntegerField()
    descuento_wt=models.IntegerField()
    subtotal_wt=models.IntegerField()
    receta_wt=models.ForeignKey(Receta, null=True, blank=True, on_delete=models.CASCADE)
    medicamento_wt=models.ForeignKey(Medicamento, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self) -> str:
        fila="{0} => {1} => {2} => {3} => {4} => {5}"
        return fila.format(self.idDetalle_wt,self.precioUnitario_wt,self.descuento_wt,self.subtotal_wt,self.receta_wt,self.medicamento_wt)